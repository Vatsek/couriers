from glob import glob
def create_files_list():
    files_lst = glob("*.csv")  # создает список из всех файлов CSV в папке.
    for i in files_lst:
        if "result" in i:
            files_lst.remove(i)
    return files_lst