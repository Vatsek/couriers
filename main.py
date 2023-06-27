import pandas as pd
from del_rows import delRows, delColumns
from create_file import create_file
from create_files_list import create_files_list
from save_to_file import save_to_file
from filter import filter

# создаем список файлов --- готово !!!!!!!!!!!
files_lst = create_files_list()


# удаляем во всех файлах шапку  --- готово!!!!!!!!!!!!!!!
for i in files_lst:
    create_file(delRows(i), i)

test = delColumns(files_lst) # вроде как работает. Возвращает список из data !!
# print(test)


# # # объединяем все dataFrame в единое целое. Вроде как работает!
result = pd.DataFrame()
for i in test:
    result = pd.concat([result, i])

result = filter(result)
print(result)
save_to_file(result)


