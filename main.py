import json
from search import *


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    with open("3-CET4-顺序.json", "r") as json_file:
        CET4 = json.load(json_file)
    with open("4-CET6-顺序.json", "r") as json_file:
        CET6 = json.load(json_file)
    with open("5-考研-顺序.json", "r") as json_file:
        RES = json.load(json_file)

    result1 = search_by_number_of_letters(number, data)

    result2 = Search_by_letter_that_determines_position(letter_position, result1)

    result3 = Search_by_existing_letters(existing_letters, result2)

    result4 = Exclude_by_nonexistent_letters(nonexistent_letters, result3)
