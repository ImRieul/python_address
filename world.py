import os.path
import time

import config
from main.entity.dataframe.excel import ExcelConfig, Excel
from main.entity.model.address import Address
from main.respository.address_repository import AddressRepository


# TODO
#   1. 엑셀 읽기
#   2. 읽은 엑셀로 주소 검색
#   3. 다시 엑셀에 저장
#   4. 검색에 성공한 주소는 address_record.xlsx로 저장
#   5. 시, 구, 동 같은 걸 따로 저장해서 문자열에 있으면 바로 사용. address_diary.xlsx

def is_excel_file(file_name: str) -> bool:
    """
    입력한 경로에 엑셀 파일이 있는지 확인

    :param file_name: path를 포함한 엑셀 파일 이름
    :return: 엑셀 파일 여부
    """
    root_file_name = config.root_path(file_name)

    if file_name not in os.listdir(os.path.dirname(root_file_name)):
        return False

    if not file_name.endswith('.xlsx'):
        return False

    return True


def input_excel_name() -> str:
    """
    엑셀 파일 이름을 입력받는 함숫

    :return: 엑셀 파일 이름
    """
    file_name = 'hello find_address'

    while not is_excel_file(file_name):
        file_name = input('사용할 엑셀 파일 이름을 입력해주세요. Ex) sample.xlsx\n >>> ')

        # 프로그램 탈출
        if file_name == 'exit':
            print('프로그램을 종료합니다.')
            time.sleep(2)
            exit()

    return file_name


excel_column = {
    'road_address_fullname': '',
    'lot_name': '',
    'legal_code': '',
    'dong_admin': '',
}


if __name__ == '__main__':
    # 엑셀 파일 입력 받기
    excel = Excel(input_excel_name())
    input(f'불러온 엑셀의 column는 다음과 같습니다\n'
          f'{list(excel.column.keys())}\n'
          f'검색할 주소, 지번 주소, 도로명 주소 열을 입력해주세요')
