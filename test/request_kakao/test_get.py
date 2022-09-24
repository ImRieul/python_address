import unittest

from main.request_kakao import RequestKakao


class testGet(unittest.TestCase):
    def test_(self):
        # given
        url = 'https://www.naver.com'
        headers = {'hello': 'world'}
        query = None

        # when
        request_kakao = RequestKakao.get(url, headers, query)

        # then
        print(request_kakao)
