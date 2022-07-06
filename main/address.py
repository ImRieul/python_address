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
        try:
            if len(self.data.json()['documents']) != 0:  # 값을 찾았을 때
                self.address = self.data.json()['documents'][0]['address']
                self.road_address = self.data.json()['documents'][0]['road_address']
        except Exception as e:
            pass


if __name__ == '__main__':
    search = '대전 서구 둔산로 100'
    address = Address(query=search)
    print(address.data)
    print(address.address)
    print(address.road_address)