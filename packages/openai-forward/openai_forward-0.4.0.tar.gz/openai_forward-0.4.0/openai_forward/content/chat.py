import time
import uuid
from typing import List

import orjson
from fastapi import Request
from loguru import logger
from orjson import JSONDecodeError

from .decode import parse_to_lines


class ChatSaver:
    def __init__(self):
        self.logger = logger.bind(chat=True)

    @staticmethod
    async def parse_payload(request: Request):
        uid = uuid.uuid4().__str__()
        payload = await request.json()
        msgs = payload["messages"]
        model = payload["model"]
        content = {
            "messages": [{msg["role"]: msg["content"]} for msg in msgs],
            "model": model,
            "forwarded-for": request.headers.get("x-forwarded-for") or "",
            "uid": uid,
            "datetime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        }
        return content

    def parse_iter_bytes(self, byte_list: List[bytes]):
        txt_lines = parse_to_lines(byte_list)

        start_line = txt_lines[0]
        target_info = dict()
        start_token = "data: "
        start_token_len = len(start_token)
        if start_line.startswith(start_token):
            stream = True
            start_line = orjson.loads(start_line[start_token_len:])
            msg = start_line["choices"][0]["delta"]
        else:
            stream = False
            start_line = orjson.loads("".join(txt_lines))
            msg = start_line["choices"][0]["message"]

        target_info["created"] = start_line["created"]
        target_info["id"] = start_line["id"]
        target_info["model"] = start_line["model"]
        target_info["role"] = msg["role"]
        target_info["content"] = msg.get("content", "")

        if not stream:
            return target_info

        # loop for stream
        for line in txt_lines[1:]:
            if line.startswith(start_token):
                target_info["content"] += self._parse_one_line(line[start_token_len:])
        return target_info

    @staticmethod
    def _parse_one_line(line: str):
        try:
            line_dict = orjson.loads(line)
            return line_dict["choices"][0]["delta"]["content"]
        except JSONDecodeError:
            return ""
        except KeyError:
            return ""

    def add_chat(self, chat_info: dict):
        self.logger.debug(f"{chat_info}")
