def create_file(list, file):
    with open(file, 'w+', encoding='utf-8-sig') as data_new:
        for i in list:
            data_new.writelines(i)





