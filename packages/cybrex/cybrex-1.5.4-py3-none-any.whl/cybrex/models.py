from typing import List

from ctransformers import AutoModelForCausalLM
from keybert import KeyBERT
from langchain import OpenAI
from langchain.embeddings import (
    HuggingFaceInstructEmbeddings,
    OpenAIEmbeddings,
)
from langchain.text_splitter import RecursiveCharacterTextSplitter
from lazy import lazy

from .llm import LLMManager
from .prompts.base import BasePrompter


def get_embedding_function(model_name):
    if model_name.startswith('hkunlp/instructor'):
        return HuggingFaceInstructEmbeddings(
            model_name=model_name,
            embed_instruction="Represent science paragraph for retrieval",
            query_instruction="Represent science question for retrieval",
        )
    elif model_name == "text-embedding-ada-002":
        return OpenAIEmbeddings(model=model_name)
    else:
        raise ValueError("Unsupported embedding model")


class CybrexModel:
    def __init__(self, config):
        self.config = config
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.config['text_splitter']['chunk_size'],
            chunk_overlap=self.config['text_splitter']['chunk_overlap'],
        )

    @classmethod
    def standard_embedders(cls, name):
        return {
            'instructor-xl': {
                'model_name': 'hkunlp/instructor-xl',
                'model_type': 'instructor',
            },
            'openai': {
                'model_name': 'text-embedding-ada-002',
                'model_type': 'openai'
            }
        }[name]

    @classmethod
    def standard_llms(cls, name):
        return {
            'llama-2-7b': {
                'max_prompt_chars': int(4096 * 2.5),
                'config': {
                    'context_length': 4096,
                    'max_new_tokens': 512,
                    'model_path_or_repo_id': 'TheBloke/Llama-2-7B-Chat-GGML',
                    'model_file': 'llama-2-7b-chat.ggmlv3.q4_K_S.bin',
                },
                'model_type': 'llama',
                'prompter': {
                    'type': 'llama-7b'
                }
            },
            'llama-2-7b-uncensored': {
                'max_prompt_chars': int(4096 * 2.5),
                'config': {
                    'context_length': 4096,
                    'max_new_tokens': 512,
                    'model_path_or_repo_id': 'TheBloke/Luna-AI-Llama2-Uncensored-GGML',
                    'model_file': 'luna-ai-llama2-uncensored.ggmlv3.q4_K_S.bin',
                },
                'model_type': 'llama',
                'prompter': {
                    'type': 'default'
                },
            },
            'llama-2-13b': {
                'max_prompt_chars': int(4096 * 2.5),
                'config': {
                    'context_length': 4096,
                    'max_new_tokens': 512,
                    'model_file': 'llama-2-13b-chat.ggmlv3.q4_K_S.bin',
                    'model_path_or_repo_id': 'TheBloke/Llama-2-13B-chat-GGML',
                },
                'model_type': 'llama',
                'prompter': {
                    'type': 'llama-7b'
                },
            },
            'openai': {
                'max_prompt_chars': int(4096 * 3.5),
                'config': {
                    'context_length': 4096,
                }
            },
        }[name]

    @classmethod
    def default_config(cls, llm_name: str = 'llama-2-7b-uncensored', embedder_name: str = 'instructor-xl'):
        return {
            'text_splitter': {
                'chunk_size': 1024,
                'chunk_overlap': 128,
                'type': 'rcts',
            },
            'embedder': cls.standard_embedders(embedder_name),
            'llm': cls.standard_llms(llm_name)
        }

    @lazy
    def keyword_extractor(self):
        return KeyBERT()

    @lazy
    def embedder(self):
        if self.config['embedder']['model_type'] == 'instructor':
            return HuggingFaceInstructEmbeddings(
                model_name=self.config['embedder']['model_name'],
                embed_instruction="Represent science paragraph for retrieval",
                query_instruction="Represent science question for retrieval",
            )
        elif self.config['embedder']['model_type'] == 'openai':
            return OpenAIEmbeddings(model=self.config['embedder']['model_name'])
        else:
            raise ValueError("Unsupported embedding model")

    @lazy
    def llm(self):
        if self.config['llm']['model_type'] == 'llama':
            return LLMManager(
                llm=AutoModelForCausalLM.from_pretrained(**self.config['llm']['config']),
                prompter=BasePrompter.prompter_from_type(self.config['llm']['prompter']['type']),
                config=self.config['llm']['config'],
                max_prompt_chars=self.config['llm']['max_prompt_chars'],
            )
        elif self.config['llm']['model_type'] == 'openai':
            return LLMManager(
                llm=OpenAI(**self.config['llm']['config']),
                prompter=BasePrompter.prompter_from_type(self.config['llm']['prompter']['type']),
                config=self.config['llm']['config'],
                max_prompt_chars=self.config['llm']['max_prompt_chars'],
            )

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """
        Embed texts into vectors using selected models

        :param texts: a list of texts
        :return: list of vectors
        """
        return self.embedder.embed_documents(texts)

    def get_embeddings_id(self):
        text_splitter_id = f'{self.config["text_splitter"]["type"]}' \
                           f'-{self.config["text_splitter"]["chunk_size"]}' \
                           f'-{self.config["text_splitter"]["chunk_overlap"]}'
        embedder_id = self.config['embedder']['model_name'].replace('/', '-')
        return f"{embedder_id}-{text_splitter_id}"
