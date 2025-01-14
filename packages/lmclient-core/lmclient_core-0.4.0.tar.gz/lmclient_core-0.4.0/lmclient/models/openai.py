from __future__ import annotations

import os
from typing import cast

import openai
from openai.openai_object import OpenAIObject
from tenacity import retry, stop_after_attempt, wait_random_exponential

from lmclient.models.base import BaseChatModel
from lmclient.types import Message, Messages, ModelResponse


class OpenAIChat(BaseChatModel):
    def __init__(
        self,
        model_name: str,
        api_key: str | None = None,
        api_base: str | None = None,
        api_version: str | None = None,
        timeout: int | None = 60,
    ):
        self.model = model_name

        openai.api_type = 'open_ai'
        openai.api_base = api_base or 'https://api.openai.com/v1'
        openai.api_key = api_key or os.environ['OPENAI_API_KEY']
        openai.api_version = api_version
        self.timeout = timeout

    @retry(wait=wait_random_exponential(min=1, max=20), stop=stop_after_attempt(3))
    def chat(self, prompt: Messages | str, **kwargs) -> ModelResponse:
        if isinstance(prompt, str):
            prompt = [Message(role='user', content=prompt)]
        if self.timeout:
            kwargs['request_timeout'] = self.timeout

        response = openai.ChatCompletion.create(model=self.model, messages=prompt, **kwargs)
        response = cast(OpenAIObject, response)
        return response.to_dict_recursive()

    @retry(wait=wait_random_exponential(min=1, max=20), stop=stop_after_attempt(3))
    async def async_chat(self, prompt: Messages | str, **kwargs) -> ModelResponse:
        if isinstance(prompt, str):
            prompt = [Message(role='user', content=prompt)]
        if self.timeout:
            kwargs['request_timeout'] = self.timeout

        response = await openai.ChatCompletion.acreate(model=self.model, messages=prompt, **kwargs)
        response = cast(OpenAIObject, response)
        return response.to_dict_recursive()

    @property
    def identifier(self) -> str:
        return f'{self.__class__.__name__}({self.model})'
