from switch_menu import *

file_name = "courier.txt"

def add_courier():
    name = input("Для добавления курьера, введите ФИО курьера через пробел: ").title()
    with open(file_name, "a", encoding="utf-8") as file:
        file.writelines(name + '\n')
        print("\nКурьер " + name + " успешно добавлен.\n")


def show_couriers():
    with open(file_name, "r", encoding="utf-8") as file:
        print("\nСписок всех курьеров:")
        print(file.read())


def del_courier():
    del_name = input("Введите фамилию курьера, которого хотите удалить: ")
    with open(file_name, "r") as f:
        lines = f.readlines()
    with open(file_name, "w") as f:
        flag = False
        for line in lines:
            if line.strip("\n").lower().__contains__(del_name.lower()):
                tmp_name = line.strip("\n")
                flag = True
            if not line.strip("\n").lower().__contains__(del_name.lower()):
                f.write(line)
    if flag == True:
        print("\nКурьер " + tmp_name + " успешно удален.\n")

    else:
        print("Курьер с введённой фамилией не найден\n\n")
        del_menu()
        switch_del_menu()


