import logging
import operation
from logg import logging

def menu():
    while True:
        logging.info("start menu")
        type_num = input("1.Показать все записи\n" 
                         "2.Найти запись\n"
                         "3.Добавить запись\n"  
                         "4.Редактировать запись\n" 
                         "5.Удалить запись\n"  
                         "6.Выход\n")
        match type_num:
            case "1":
                operation.print_data()
                menu()
            case "2":
                operation.serch_record(input("Введите данные для поиска: "))
                menu()
            case "3":
                operation.add_record()
                menu()
            case "4":
                operation.edit_record(int(input("Введите ID сотрудника: ")))
                menu()
            case "5":
                operation.delete_record(int(input("Введите ID сотрудника: ")))
                menu()
            case "6":
                logging.info("menu exit")
                print("Конец работы")
                quit()
            case _:
                logging.error("error: Input Error menu")
                print("Ошибка: введите корректные данные")

menu()
