import logging
import pandas 
import csv
import codecs

def add_record():
    with open("hrdata.csv", 'a', newline= '', encoding='utf-8') as csvfile:
        line_count = sum(1 for line in open('hrdata.csv'))
        writer = csv.writer(csvfile, delimiter = ";")
        writer.writerow([line_count + 1, input("Введите имя сотрудника: "), 
                         input("Введите фамилию сотрудника: "), 
                         input("Введите должность сотрудника: "),
                         input("Введите номер телефона сотрудника: ")])


def check_availability(num):
    line_count = sum(1 for line in open('hrdata.csv'))
    while True:
        if line_count < num or num < 0:
                logging.error("error: row selection error")
                print("Ошибка: такой строки нет")
                num = input("Введите номер строки: ")
        else:
            break
    return num

def search_record(num):
    inp = iter(codecs.open('hrdata.csv', encoding='utf-8').readlines())
    for i in inp:
        if num[0] in i:
            print(i)

def print_data():  
    df = pandas.read_csv('hrdata.csv')   
    print(df)   

add_record()
# print_data()
# search_record(input())

