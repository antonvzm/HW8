import logging
import pandas 
import csv
import codecs

def add_record():
    logging.info("add record")
    with open("hrdata.csv", 'a', newline= '', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter = ",")
            writer.writerow([input("Введите имя сотрудника: "), 
                            input("Введите фамилию сотрудника: "), 
                            input("Введите должность сотрудника: ")])


def serch_record(word):
    logging.info("serch record")
    inp = iter(codecs.open('hrdata.csv', encoding='utf-8').readlines())
    for i in inp:
        if word in i:
            print(i)

def print_data():
    logging.info("print data")  
    df = pandas.read_csv('hrdata.csv')   
    print(df)   

def edit_record(num):
    logging.info("edit record")
    with open("hrdata.csv", encoding='utf-8') as file:
        array = file.readlines()
    name = input("Введите имя сотрудника: ")
    surname = input("Введите фамилию сотрудника: ")
    job = input("Введите должность сотрудника: ")
    array[num+1] = f'{name},{surname},{job}\n'
    f = open('hrdata.csv', 'w', encoding='utf-8')
    f.writelines(array) 
    f.close ()

def delete_record(num):
    logging.info("delete record")
    with open("hrdata.csv", encoding='utf-8') as file:
        array = file.readlines()
    array.pop(num+1)
    f = open('hrdata.csv', 'w', encoding='utf-8')
    f.writelines(array) 
    f.close ()


