'''
Задание 5 Реализуйте алгоритм перемешивания списка.
'''
from random import randrange
def task_enter():
    print(f'Task #{__name__[4:]}.')
    while True:
        int_num = input("Enter integer number (>= 2) or '/break' to change task: ")
        if int_num == '/break':
            return
        elif input_valid_condition(int_num):
            task_basic_func(int_num)
        else:
            print("Invalid integer. Try again.")
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def task5():
    print('Task #5.')
    while True:
        intNum = input("Enter integer number (>= 2) or '/break' to change task: ")
        if intNum == '/break':
            return
        elif int(intNum) < 2:
            print("Invalid integer. Try again.")
        else:
            sequence_list = listCreation(int(intNum))
            print(f"Before mix list - {sequence_list}.")
            print(f"After mix list - {listMix(sequence_list)}.")
#--------------------------------------------------------------------
def listCreation_old(num):
    cr_list = []
    for i in range(num):
        cr_list.append(randrange(-10, 11))
    return cr_list
#--------------------------------------------------------------------
def listMix_old(seq):
    num = len(seq)
    randIndex = None
    buffer = None
    for i in range(num):
        randIndex = randrange(num)
        buffer = seq[randIndex]
        seq[randIndex] = seq[i]
        seq[i] = buffer
    return seq
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def input_valid_condition(input_data):
    return int(input_data) >= 2
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def task_basic_func(in_data):
    sequence_list = listCreation(int(in_data))
    print(f"Before mix list - {sequence_list}.")
    print(f"After mix list - {listMix(sequence_list)}.")
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#----------------------------------------------------------------------
def listCreation(num):
    return [randrange(-10, 11) for i in range(num)]
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def listMix(seq):
    num = len(seq)
    randIndex = None
    buffer = None
    for i in range(num):
        randIndex = randrange(num)
        buffer = seq[randIndex]
        seq[randIndex] = seq[i]
        seq[i] = buffer
    return seq

