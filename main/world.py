from main.entity.dataframe.excel import ExcelConfig, Excel
from main.entity.model.address import Address
from main.respository.address_repository import AddressRepository


# TODO
#   1. 엑셀 읽기
#   2. 읽은 엑셀로 주소 검색
#   3. 다시 엑셀에 저장
#   4. 검색에 성공한 주소는 address_record.xlsx로 저장
#   5. 시, 구, 동 같은 걸 따로 저장해서 문자열에 있으면 바로 사용. address_diary.xlsx

def trimming(string: str, trim: list) -> str:
    for i in trim:
        if string.find(i) != -1 and len(string) >= string.find(i):
            string = string[:string.find(i)]

    return string


if __name__ == '__main__':
    cut_string_list = [',', '.', '지하', '층', '호', '상가동', '상가', '(', '***', '인근']

    address = AddressRepository().find_by_search('둔산로 100')
    hello = trimming(address.road_address_fullname, cut_string_list)
    print(hello)

