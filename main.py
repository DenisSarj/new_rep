
with open('file1', 'rt', encoding='utf-8') as eat_book:
    res = {}
    for line in eat_book:
        name_cook = line.strip()
        count_cook = int(eat_book.readline())
        ingridient = []
        for _ in range(count_cook):
            split_ing = eat_book.readline().strip().split(' | ')
            name_ing, count_ing, mesuare = split_ing
            ingridient.append({'name_ing': name_ing,
                               'quantity': int(count_ing),
                               'measure': mesuare})
        eat_book.readline()
        res[name_cook] = ingridient
print(res)

S = ['Омлет', 'Утка по-пекински']
def amount (cook_book, quan=1):
    list = []
    dict_1 = {}
    dict_2 = {}
    for cook in cook_book:
        list.append(res[cook])
    for lists in list:
        for dicts in lists:
            key = dicts['name_ing']
            if dict_2.get(key, False) is False:
                dict_2[key] = dicts['quantity']
            else:
                dict_2[key] += dicts['quantity']
            dict_1[dicts['name_ing']] = {'meas': dicts['measure'], 'quan': quan * dict_2[key]}
    print(dict_1)
amount(S)





