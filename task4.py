'''
Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на позициях a и b.
Значения N, a и b вводит пользователь с клавиатуры.
'''
from random import randrange

def task_enter():
    print(f'Task #{__name__[4:]}.')
    while True:
        int_num = input("Enter positive integer number or '/break' to change task: ")
        if int_num == '/break':
            return
        elif input_valid_condition(int_num):
            task_basic_func(int_num)
        else:
            print("Invalid integer. Try again.")
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def task4_old():
    print('Task #4.')
    while True:
        intNum = input("Enter positive integer number or '/break' to change task: ")
        if intNum == '/break':
            return
        elif int(intNum) < 1:
            print("Invalid integer. Try again.")
        else:
            sequence_list = seqMinPl(int(intNum))
            print(f"The sequence from {-1*intNum} to {intNum} is {sequence_list}.")
            print(f"Multiplication result is {prodProc(sequence_list)}.")
#--------------------------------------------------------------------
def seqMinPl_old(num):
    mp_list = []
    for i in range(num ):
        mp_list.append(randrange(-num, num+1))
    return mp_list
#--------------------------------------------------------------------
def prodProc_old(seq):
    max = len(seq)
    while True:
        a = int(input("Enter position of the first multiplier: "))
        if (a >= max) or (a < 0):
            print("Invalid position. Try again.")
            continue
        b = int(input("Enter position of the second multiplier: "))
        if (b >= max) or (b < 0):
            print("Invalid position. Try again.")
            continue
        break
    return seq[a] * seq[b]
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def input_valid_condition(input_data):
    return int(input_data) >= 1  
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#----------------------------------------------------------------------
def task_basic_func(in_data):
    sequence_list = seqMinPl(int(in_data))
    print(f"The sequence from {-1*in_data} to {in_data} is {sequence_list}.")
    print(f"Multiplication result is {prodProc(sequence_list)}.")
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#----------------------------------------------------------------------
def seqMinPl(num):
    return [randrange(-num, num+1) for i in range(num)]
#--------------------------------------------------------------------
def prodProc(seq):
    max = len(seq)
    while True:
        a = int(input("Enter position of the first multiplier: "))
        if (a >= max) or (a < 0):
            print("Invalid position. Try again.")
            continue
        b = int(input("Enter position of the second multiplier: "))
        if (b >= max) or (b < 0):
            print("Invalid position. Try again.")
            continue
        break
    return seq[a] * seq[b]
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#----------------------------------------------------------------------