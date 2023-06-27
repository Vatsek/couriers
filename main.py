import pandas as pd
from del_rows import delRows, delColumns
from create_file import create_file
from create_files_list import create_files_list

# создаем список файлов --- готово !!!!!!!!!!!
files_lst = create_files_list()


# # удаляем во всех файлах шапку  --- готово!!!!!!!!!!!!!!!
# for i in files_lst:
#     create_file(delRows(i), i)

test = delColumns(files_lst) # вроде как работает. Возвращает список из data !!
# print(test)


# # # объединяем все dataFrame в единое целое. Вроде как работает!
result = pd.DataFrame()
for i in test:
    result = pd.concat([result, i])

result = result.drop_duplicates(['Номер ЗК'])

result = result.groupby(['Дата выполнения ЗК','ФИО курьера']).size()
print(result)


# #
# # # print(type(general_data))
# # # result = result[['Дата выполнения ЗК','ФИО курьера']]
# result = result.groupby(['Дата выполнения ЗК','ФИО курьера']).size()
# result.to_csv('result.csv', index=False)
# #
#
#
