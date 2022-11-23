from main.entity.model.address import Address
from main.entity.dataframe.excel import Excel


def _slice(search: str):
    excel_slice = Excel('address_slice.xlsx')

    for index, word in enumerate(excel_slice.column['word']):
        if search.find(word) != -1:
            word_left = search[search.find(word) - 1]
            word_right = search[search.find(word) + len(word)]

            # end option. 끝 단어가 word로 끝나는지 검사.
            if excel_slice.column['end'][index] == 1:
                if word_right != ' ':
                    continue

            # only option.
            # 값이 있으면 해당 단어 뒤로 날리고
            # 값이 없으면 해당 단어를 포함한 값을 날린다.
            if excel_slice.column['only'][index] == 1:
                search = ''.join(search.split(word)[0])
            else:
                word_slice = [index for index, value in enumerate(search.split(' ')) if value.find(word) != -1][0]
                search = ' '.join(search.split(' ')[:word_slice])

    return search


if __name__ == '__main__':
    address = _slice('대전 서구 둔산로 100 100호 (둔산동, 대전광역시시청)')
    print(address)
