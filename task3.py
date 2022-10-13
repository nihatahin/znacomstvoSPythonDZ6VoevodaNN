'''Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
округлённую до трёх знаков после точки.

Пример:

Для n = 6 -> 14.072
'''
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
def task3_old():
    print('Task #3.')
    while True:
        intNum = input("Enter positive integer number or '/break' to change task: ")
        if intNum == '/break':
            return
        elif int(intNum) < 1:
            print("Invalid integer. Try again.")
        else:
            sequence = seqList(int(intNum))
            print(f'The (1+1/n)^n subsequence list of {intNum} numbers is {sequence}.')
            print(f'The rounded sum of numbers is {sumSeqList(sequence)}.')
#--------------------------------------------------------------------
def seqList_old(num):
    s_list = []
    for i in range(1, num + 1):
        s_list.append(round((1+1/i)**i, 3))
    return s_list
#--------------------------------------------------------------------
def sumSeqList_old(seq):
    sum = 0
    for i in range(len(seq)):
        sum += seq[i]
    return sum
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def input_valid_condition(input_data):
    return int(input_data) >= 1
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def task_basic_func(in_data):
    sequence = seqList(int(in_data))
    print(f'The (1+1/n)^n subsequence list of {in_data} numbers is {sequence}.')
    print(f'The rounded sum of numbers is {sumSeqList(sequence)}.')
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#----------------------------------------------------------------------
def seqList(num):
    s_list = [i for i in range(1, num + 1)]
    return list(map(lambda x: round((1+1/x)**x, 3), s_list))
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#----------------------------------------------------------------------
def sumSeqList(seq):
    sum = 0
    for i in range(len(seq)):
        sum += seq[i]
    return sum
