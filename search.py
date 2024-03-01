def search_by_number_of_letters(number, data):
    result = []
    for i in data:
        if len(i['word']) == number:
            result.append(i['word'])
    return result


def Search_by_letter_that_determines_position(letter_position, data):
    result = []
    for i in data:
        t = 0
        for j in letter_position:
            if i[j[0] - 1] != j[1]:
                t = 1
                break
        if t == 1:
            continue
        result.append(i)
    return result


def Search_by_existing_letters(existing_letters, data):
    result = []
    for i in data:
        t = 0
        for j in existing_letters:
            if j in i:
                continue
            else:
                t = 1
                break
        if t == 1:
            continue
        result.append(i)
    return result


def Exclude_by_nonexistent_letters(nonexistent_letters, data):
    result = []
    t = 0
    for i in data:
        for j in nonexistent_letters:
            if j in i:
                t = 1
                break
        if t == 1:
            continue
        result.append(i)
    return result
