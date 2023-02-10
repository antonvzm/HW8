import logging
import operation

def menu():
    while True:
        type_num = input("1.Показать все записи\n" 
                         "2.Найти запись\n"
                         "3.Добавить запись\n"  
                         "4.Редактировать запись\n" 
                         "5.Удалить запись\n" 
                         "6.Экспорт/Импорт\n" 
                         "7.Выход\n")
        f = open('base.txt')
        match type_num:
            case "1"|"3"|"4"|"5"|"6":
                print(f.read())
                menu()
            # case "2":
            #     menu_calc(type_num)
            #     break
            # case "3":
            #     menu_calc(type_num)
            #     break
            # case "4":
            #     menu_calc(type_num)
            #     break
            # case "5":
            #     menu_calc(type_num)
            #     break
            # case "6":
            #     menu_calc(type_num)
            #     break
            case "7":
                logging.info("menu exit")
                print("Конец работы")
                break
            case _:
                logging.error("error: Input Error menu")
                print("Ошибка: введите корректные данные")

menu()
