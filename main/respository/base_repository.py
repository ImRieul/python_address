from __future__ import annotations

import requests
from requests import JSONDecodeError

import setting
from main.logger import Logger


class BaseRepository:
    def __init__(self,
                 url: str,
                 ):
        self._url = url
        self._response = None
        self._status = 404
        self._logger = Logger()
        self._body = {}

    def get(self, query: dict = None, headers: dict = None):
        request = self._url

        if query is not None:
            request += '?' + ''.join([key + '=' + value + '&' for key, value in query.items()])[:-1]

        self._response = requests.get(request, headers=headers)
        self._status = self._response.status_code

        try:
            self._body = self._response.json()
        except JSONDecodeError as json_error:
            self._logger.error('requests error, if request page is html')
            self._body = {}

    @property
    def response(self):
        return self._response

    @property
    def status(self):
        return self._status


if __name__ == '__main__':
    test = BaseRepository('https://dapi.kakao.com/v2/local/search/address')
    test.get({'query': '배재로 128'}, {'Authorization': setting.KAKAO_TOKEN})
