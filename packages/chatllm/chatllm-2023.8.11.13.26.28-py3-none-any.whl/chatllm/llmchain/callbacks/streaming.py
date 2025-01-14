#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : streaming
# @Time         : 2023/7/11 10:03
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  :

from queue import Queue
from threading import Event
from typing import Any, Generator, Union

from langchain.callbacks.base import BaseCallbackHandler, LLMResult


class StreamingGeneratorCallbackHandler(BaseCallbackHandler):
    """Streaming callback handler."""

    def __init__(self) -> None:
        self._token_queue: Queue = Queue()
        self._done = Event()

    def __deepcopy__(self, memo: Any) -> "StreamingGeneratorCallbackHandler":
        # NOTE: hack to bypass deepcopy in langchain
        return self

    def on_llm_new_token(self, token: str, **kwargs: Any) -> Any:
        """Run on new LLM token. Only available when streaming is enabled."""
        self._token_queue.put_nowait(token)

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        self._done.set()

    def on_llm_error(
        self, error: Union[Exception, KeyboardInterrupt], **kwargs: Any
    ) -> None:
        self._done.set()

    def get_response_gen(self) -> Generator:
        while True:
            if not self._token_queue.empty():
                token = self._token_queue.get_nowait()
                # from loguru import logger
                # logger.debug(token)

                yield token
            elif self._done.is_set():
                break
