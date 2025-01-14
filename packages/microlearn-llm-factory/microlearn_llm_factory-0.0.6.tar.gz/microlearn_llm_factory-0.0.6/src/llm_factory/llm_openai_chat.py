"""
LLM wrapper for OpenAI chat model.
"""
import promptlayer  # Do not remove this line.
from langchain.callbacks import PromptLayerCallbackHandler
from langchain.chat_models import ChatOpenAI

from llm_factory.llm_base import LLMBase


class LLMOpenAIChat(LLMBase):
    """
    LLM wrapper for OpenAI chat model.
    """

    def _validate_args(self, **kwargs):
        assert "model_name" in kwargs, "'model_name' must be provided"
        assert "temperature" in kwargs, "'temperature' must be provided"
        assert "max_tokens" in kwargs, "'max_tokens' must be provided"
        if "verbose" in kwargs:
            assert isinstance(kwargs["verbose"],
                              bool), "'verbose' must be a boolean"
        if "pl_tags" in kwargs:
            assert isinstance(kwargs["pl_tags"],
                              list), "'pl_tags' must be a list"
            for tag in kwargs["pl_tags"]:
                assert isinstance(
                    tag, str), "'pl_tags' must be a list of strings"

    def _build_llm(self, **kwargs):
        if "pl_tags" in kwargs:
            llm = ChatOpenAI(
                model=kwargs["model_name"],
                temperature=kwargs["temperature"],
                max_tokens=kwargs["max_tokens"],
                verbose=kwargs.get("verbose", False),
                callbacks=[PromptLayerCallbackHandler(
                    pl_tags=kwargs.get("pl_tags", []))
                ],
            )
        else:
            llm = ChatOpenAI(
                model=kwargs["model_name"],
                temperature=kwargs["temperature"],
                max_tokens=kwargs["max_tokens"],
                verbose=kwargs.get("verbose", False),
            )
        return llm

    @staticmethod
    def get_default_args():
        return {
            "model_name": "gpt-4",
            "temperature": 0,
            "max_tokens": 256,
        }
