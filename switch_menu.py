from list_of_couriers import *
from menu import *

def switch_main_menu(command):
        match command:
            case "1":
                show_couriers()
            case "2":
                add_courier()
            case "3":
                del_courier()
            case "4":
                print("Создать отчет")
            case "5":
                exit()
            case _:
                print("Неверный ввод команды")

def switch_del_menu(command):
    match command:
        case "1":
            del_courier()
        case "2":
            main_menu()
        case "3":
            exit()
        case _: print("Не верно введен номер команды")

while True:
    main_menu()
    switch_main_menu(input("Введиете номер команды: "))