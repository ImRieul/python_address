from __future__ import annotations

import requests


class RequestKakao:
    def __init__(self):
        self.response = None
        self.request_url: str = ''  # 기록용 변수 저장
        self.headers: dict = {}  # 기록용 변수 저장

    def get(self, url: str, headers: dict, query: dict) -> RequestKakao:
        self.request_url = url
        self.headers = headers

        if len(query.items()) != 0:
            self.request_url += '?'
            self.request_url += ''.join([key + '=' + value + '&' for key, value in query.items()])[:-1]

        self.response = requests.get(
            url=self.request_url,
            headers=headers
        )

        return self
