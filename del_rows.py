def delRows(file):
    count = 0
    new_list = []
    with open(file, 'r', encoding="utf-8") as data:
        for line in data:
            count += 1
            if count > 7:
                result = line.split(';')
                new_list.append(result)
        return new_list