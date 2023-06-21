import pandas as pd
from del_rows import delRows
from create_file import create_file
from create_files_list import create_files_list
# k = pd.read_csv('k1.csv', encoding="utf-8", delimiter = ';')

# k2 = pd.read_csv('k2.csv', encoding="utf-8", delimiter = ';')
# print(k2.count())

# создаем список файлов
files_lst = create_files_list()


# удаляем во всех файлах шапку
for i in files_lst:
    create_file(delRows(i), i)

# объединяем все файлы в единое целое
general_data = pd.concat(
    map(pd.read_csv, files_lst), ignore_index=True)
print(general_data)
