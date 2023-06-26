import pandas as pd
from del_rows import delRows
from create_file import create_file
from create_files_list import create_files_list

# создаем список файлов
files_lst = create_files_list()


# удаляем во всех файлах шапку
for i in files_lst:
    create_file(delRows(i), i)

# объединяем все файлы в единое целое
result = pd.DataFrame()
print(type(result))
for file in files_lst:
    data = pd.read_csv(file)
    result = pd.concat([result, data])
print(result)
# print(type(general_data))
# result = result[['Дата выполнения ЗК','ФИО курьера']]
# result = result.groupby(['Дата выполнения ЗК','ФИО курьера']).size()
result.to_csv('result.csv', index=False, sep=';')



