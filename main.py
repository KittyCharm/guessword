import json
from search import *

# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    with open("3-CET4-顺序.json", "r", encoding="utf-8") as json_file:
        CET4 = json.load(json_file)

    with open("4-CET6-顺序.json", "r", encoding="utf-8") as json_file:
        CET6 = json.load(json_file)
    with open("5-考研-顺序.json", "r", encoding="utf-8") as json_file:
        RES = json.load(json_file)

    number = 10
    data = RES
    result1 = search_by_number_of_letters(number, data)
    # print(result1)

    letter_position = [[9,'o'],[1,'i'],[2,'n'],[6,'a']]
    result2 = Search_by_letter_that_determines_position(letter_position, result1)
    # print(result2)

    existing_letters = ''
    result3 = Search_by_existing_letters(existing_letters, result2)
    # print(result3)

    nonexistent_letters_may = ''

    nonexistent_letters=''
    for i in nonexistent_letters_may:
        if i in existing_letters:
            continue
        nonexistent_letters=nonexistent_letters+i

    result4 = Exclude_by_nonexistent_letters(nonexistent_letters, result3)
    print(result4)
