import os
from main.entity.dataframe.excel import *

import unicodedata

from main.personal.tools import list_insert

'''
생각보다 내가 만든 라이브러리 Excel이 쓰기 불편했다.
맥과 윈도우의 호환도 힘들고 (윈도우 파일 이름이 맥에서 깨짐)
2차원으로 데이터를 입력할 수가 없다. (list_insert를 억지로 이용)
1개의 column list는 뽑아올 수 있지만, 그와 같은 row의 다른 column list는 다루기 어려웠다.
python의 편의성 때문에 이용할만하지, cells(1, 1).value와 같은 수준은 안 되는 거 같다.

VBA처럼 range, cell같은 객체를 직접 만드는 게 나을 수도 있겠다.
나중에 리팩토링할 수 있도록 코드마다 주석을 달아놓았다.
'''


def slice_file_name(file: str) -> str:
    '''
    번호, 확장자를 제거하는 함수
    :param file: '번호.파일이름.확장자'
    :return: '파일이름'
    '''
    if file.find('.') == -1:
        response = file
    else:
        response = file.split('.')[1]

    # 맥은 한글로 된 파일 이름이 ㄱㅣㅁㄷㅗㅇㄱㅓㄴ.xlsx로 저징되므로, 김동건.xlsx로 만들어주기 위한 라이브러리
    return unicodedata.normalize('NFC', response)


if __name__ == '__main__':
    excel_list_xlsx: list[str] = list(filter(lambda x: x.find(".xlsx") != -1 and x.find("$") == -1, os.listdir()))
    excel_list = list(map(lambda x: x.split('.')[1], excel_list_xlsx))

    excel_config = ExcelConfig(file_name="world_column_count/컬럼정의서.xlsx",
                               standard_row=4,
                               standard_column=1)

    excel_name: str = "테이블명(한글)"  # 읽을 엑셀파일 이름
    column_name: str = "컬럼 한글명"  # 읽을 Column 이름
    value_name: str = "데이터 수"  # 입력할 Column 이름

    work_excel = Excel(excel_config)

    # check_excel = work_excel.get_column_data(column_name=excel_name)
    # print(work_excel.column_with_index(excel_name))

    for excel in excel_list_xlsx:
        if excel.find('$') != -1:  # 현재 읽는 중인 Excel 파일은 제외
            continue
        file_name = slice_file_name(excel)  # 전체 파일 이름에서 필요한 이름만 가져오기
        cell_config = ExcelConfig(file_name="world_column_count/" + excel)
        search_excel = Excel(cell_config)

        search_index = list(
            filter(lambda x: x[1] == file_name, work_excel.column_with_index(excel_name)))  # work_excel의 수정할 row 추출
        search_index = list(map(lambda x: x[0], search_index))  # work_excel의 수정할 row index 추출
        print(file_name, search_index)  # log

        for index in search_index:
            search_column = work_excel.column[column_name][index]  # search_excel에서 읽을 Column 추출

            if search_column == '순번':
                # 이상하게 순번은 읽지 못해서 따로 기록해줌 (전체 column 개수를 가져오면 되므로)
                counta = len(search_excel.column[search_column])
            else:
                # 비어있지 않은 셀만 세기
                counta = len(list(filter(lambda x: x != '', search_excel.column[search_column])))

            # 수정할 row에 추가.
            work_excel.row[index] = list_insert(work_excel.row[index], [counta], 4, True)

    work_excel.save()
