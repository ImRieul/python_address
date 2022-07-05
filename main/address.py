import setting
import requests


class Address:
    def __init__(self, **query):
        self.url = 'https://dapi.kakao.com/v2/local/search/address'
        self.query = query
        self.data = None
        self.address = None
        self.road_address = None
        self.__get_data()
        self.__get_address()

    def __get_data(self):
        request_url = '?' + ''.join([i + '=' + self.query[i] + '/' for i in self.query])[:-1]
        self.data = requests.get(self.url + request_url, headers={'Authorization': setting.KAKAO_TOKEN})
        # return self.data

    def __get_address(self):
        if self.data is None:
            self.address = None
        elif self.data.status_code == 400:
            self.address = None
        elif len(self.data.json()['documents']) != 0:  # 값을 찾았을 때
            self.address = self.data.json()['documents'][0]['address']
            self.road_address = self.data.json()['documents'][0]['road_address']
        # return self.address
