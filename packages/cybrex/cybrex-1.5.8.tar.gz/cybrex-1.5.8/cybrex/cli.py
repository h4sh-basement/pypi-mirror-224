import json
import logging
import re
import sys
import textwrap
from typing import Optional

import fire
from termcolor import colored

from .cybrex_ai import CybrexAI


def create_snippet(document):
    return document['metadata']['id'] + ': ' + document['text']


class CybrexCli:
    def __init__(self, cybrex: Optional[CybrexAI] = None):
        self.cybrex = cybrex or CybrexAI()

    async def add_all_documents(self):
        async with self.cybrex as cybrex:
            async for document in cybrex.geck.get_summa_client().documents('nexus_science'):
                document = json.loads(document)
                await self.cybrex.upsert_documents([document])

    async def export_chunks(self, query: str, output_path: str, n_documents: int = 10):
        """
        Store STC text chunks in ZIP archive

        :param query: query to STC
        :param output_path: where to store result
        :param n_documents: the number of chunks to extract
        """
        async with self.cybrex as cybrex:
            print(f"{colored('Q', 'green')}: {query}")
            await cybrex.export_chunks(
                query=query,
                output_path=output_path,
                n_documents=n_documents
            )

    async def chat_doc(self, document_query: str, query: str, n_chunks: int = 5):
        """
        Ask a question about content of document identified by DOI.

        :param document_query: query that returns unique document
        :param query: Text query to the document
        :param n_chunks: the number of chunks to extract from Chroma
            more means more tokens to use and more precision in answer
        """
        async with self.cybrex as cybrex:
            print(f"{colored('Document', 'green')}: {document_query}")
            print(f"{colored('Q', 'green')}: {query}")
            answer, _ = await cybrex.chat_document(document_query, query, n_chunks)
            print(f"{colored('A', 'green')}: {answer}")

    async def chat_sci(
        self,
        query: str,
        n_chunks: int = 5,
        n_documents: int = 10,
    ):
        """
        Ask a general questions

        :param query: text query to the document
        :param n_chunks: the number of chunks to extract from Chroma
            more means more tokens to use and more precision in answer
        :param n_documents: the number of chunks to extract from Chroma
            more means more tokens to use and more precision in answer
        """
        async with self.cybrex as cybrex:
            print(f"{colored('Q', 'green')}: {query}")
            answer, chunks = await cybrex.chat_science(
                query=query,
                n_chunks=n_chunks,
                n_documents=n_documents,
            )
            answer = re.sub(r'\(DOI: ([^)]+)\)', r'(https://doi.org/\g<1>)', answer)
            documents = await self.cybrex.get_documents_from_chunks(chunks)
            documents = [
                f'{document.get("doi") or document.get("metadata", {}).get("isbns")}: {document["title"]}'
                for document in documents
            ]
            sources = '\n'.join(documents)
            print(f"{colored('A', 'green')}: {answer}")
            print(f"{colored('References', 'green')}:\n{textwrap.indent(sources, ' - ')}")

    async def sum_doc(self, document_query: str):
        """
        Summarization of the document

        :param document_query: query that returns unique document
        """
        async with self.cybrex as cybrex:
            print(f"{colored('Document', 'green')}: {document_query}")
            answer, _ = await cybrex.summarize_document(document_query)
            print(f"{colored('Summarization', 'green')}: {answer}")

    async def semantic_search(self, query: str, n_chunks: int = 5, n_documents: int = 10):
        """
        Search related to query text chunks among `n` documents

        :param query: query to STC
        :param n_chunks: number of chunks to return
        :param n_documents: the number of documents to extract from STC
        """
        async with self.cybrex as cybrex:
            print(f"{colored('Q', 'green')}: {query}")
            chunks = await cybrex.semantic_search(
                query=query,
                n_chunks=n_chunks,
                n_documents=n_documents
            )
            snippets = [
                ' - ' + create_snippet(chunk)
                for chunk in chunks
            ]
            sources = '\n'.join(snippets)
            print(f"{colored('Sources', 'green')}:\n{sources}")


def cybrex_cli(debug: bool = False):
    """
    :param debug: add debugging output
    :return:
    """
    logging.basicConfig(stream=sys.stdout, level=logging.INFO if debug else logging.ERROR)
    cybrex_ai = CybrexCli()
    return {
        'add-all-chunks': cybrex_ai.add_all_documents,
        'chat-doc': cybrex_ai.chat_doc,
        'chat-sci': cybrex_ai.chat_sci,
        'export-chunks': cybrex_ai.export_chunks,
        'import-chunks': cybrex_ai.cybrex.import_chunks,
        'semantic-search': cybrex_ai.semantic_search,
        'sum-doc': cybrex_ai.sum_doc,
        'write-config': cybrex_ai.cybrex.write_config,
    }


def main():
    fire.Fire(cybrex_cli, name='cybrex')


if __name__ == '__main__':
    main()
