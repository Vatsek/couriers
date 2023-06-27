import pandas as pd

def delRows(file):
    count = 0
    new_list = []
    with open(file, 'r', encoding="utf-8") as data:
        for line in data:
            count += 1
            if count > 7:
                result = line
                new_list.append(result)
        return new_list

def delColumns(file_list):
    result = []
    for i in file_list:
        k = pd.read_csv(i, encoding="utf-8", delimiter=';')
        k.drop(k.columns[[0, 2, 3, 4, 6, 7, 9]], axis=1, inplace=True)
        result.append(k)
    return result





    # k.to_csv(file, index=False)



