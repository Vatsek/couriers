from glob import glob
def create_files_list():
    files_lst = glob("*.csv")  # создает список из всех файлов CSV в папке.
    print(files_lst)
    return files_lst