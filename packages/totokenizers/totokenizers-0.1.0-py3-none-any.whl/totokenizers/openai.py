import logging
from typing import Literal, Optional

import tiktoken

from .errors import ModelNotFound, ModelNotSupported
from .jsonschema_formatter import FunctionJSONSchema
from .schemas import Chat, ChatMLMessage, FunctionCallChatMLMessage, FunctionChatMLMessage

logger = logging.getLogger("totokenizers")


class OpenAITokenizer:
    funcion_header = "\n".join(
        [
            "# Tools",
            "",
            "## functions",
            "",
            "namespace functions {",
            "",
            "} // namespace functions",
        ]
    )

    def __init__(
        self,
        model_name: Literal[
            "gpt-3.5-turbo",
            "gpt-3.5-turbo-0301",
            "gpt-3.5-turbo-0613",
            "gpt-3.5-turbo-16k-0613",
            "gpt-4-0314",
            "gpt-4-32k-0314",
            "gpt-4-0613",
            "gpt-4-32k-0613",
        ],
    ):
        self.model = model_name
        try:
            self.encoder = tiktoken.encoding_for_model(model_name)
        except KeyError:
            raise ModelNotFound(model_name)
        self._init_model_params()

    def _init_model_params(self):
        """https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb"""
        if self.model == "gpt-3.5-turbo":
            logger.warning(
                "'gpt-3.5-turbo' may update over time. Returning num tokens assuming 'gpt-3.5-turbo-0613'."
            )
            self.model = "gpt-3.5-turbo-0613"
        if self.model == "gpt-4":
            logger.warning(
                "'gpt-4' may update over time. Returning num tokens assuming 'gpt-4-0613'."
            )
            self.model = "gpt-4-0613"
        if self.model in {
            "gpt-3.5-turbo-0613",
            "gpt-3.5-turbo-16k-0613",
            "gpt-4-0314",
            "gpt-4-32k-0314",
            "gpt-4-0613",
            "gpt-4-32k-0613",
        }:
            self.tokens_per_message = 3
            self.tokens_per_name = 1
        elif self.model == "gpt-3.5-turbo-0301":
            self.tokens_per_message = (
                4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
            )
            self.tokens_per_name = -1  # if there's a name, the role is omitted
        else:
            raise ModelNotSupported(self.model)

    def encode(self, text: str) -> list[int]:
        return self.encoder.encode(text)

    def count_tokens(self, text: str) -> int:
        return len(self.encode(text))

    def count_chatml_tokens(
        self, messages: Chat, functions: Optional[list[dict]] = None
    ) -> int:
        num_tokens = sum(map(self.count_message_tokens, messages))
        num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
        if functions:
            if messages[0]["role"] == "system":
                num_tokens -= 1  # I believe a newline gets removed somewhere for somereason
            else:
                num_tokens += self.tokens_per_message
            num_tokens += self.count_functions_tokens(functions)
        return num_tokens

    def count_message_tokens(self, message: ChatMLMessage | FunctionCallChatMLMessage | FunctionChatMLMessage) -> int:
        """https://github.com/openai/openai-python/blob/main/chatml.md"""
        num_tokens = self.tokens_per_message
        if message["role"] == "function":
            num_tokens += (
                self.count_tokens(message["content"])
                + self.count_tokens(message["name"])
                + self.count_tokens(message["role"])
                - 1  # omission of a delimiter?
            )
        elif "function_call" in message:
            # https://github.com/forestwanglin/openai-java/blob/308a3423d34905bd28aca976fd0f2fa030f9a3a1/jtokkit/src/main/java/xyz/felh/openai/jtokkit/utils/TikTokenUtils.java#L202-L205
            num_tokens += (
                self.count_tokens(message["function_call"]["name"])
                + self.count_tokens(message["function_call"]["arguments"])  # TODO: what if there are no arguments?
                + self.count_tokens(message["role"])
                + 3  # I believe this is due to delimiter tokens being added
            )
        else:
            num_tokens += (
                self.count_tokens(message["content"])
                + self.count_tokens(message["role"])
            )
            if "name" in message:
                num_tokens += self.tokens_per_name + self.count_tokens(message["name"])
        return num_tokens

    def count_functions_tokens(self, functions: list[dict]) -> int:
        num_tokens = len(self.encode(self.funcion_header))
        num_tokens += len(self.encode(FunctionJSONSchema(functions).to_typescript()))
        return num_tokens
