from curses.ascii import isdigit
'''
Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:

6782 -> 23
0,56 -> 11
'''
def task_enter():
    print(f'Task #{__name__[4:]}.')
    while True:
        int_num = input("Enter real number or '/break' to change task: ")
        if int_num == '/break':
            return
        else:
            task_basic_func(int_num)
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def task1_old():
    print('Task #1.')
    while True:
        realNum = input("Enter real number or '/break' to change task: ")
        if realNum == '/break':
            return
        else:
            print(f"The digit sum of {realNum} is {digitSum_old(realNum)}.")
#--------------------------------------------------------------------
def digitSum_old(num):
    sum = 0
    for i in range(len(num)):
        if isdigit(num[i]):
            sum += int(num[i])
    return sum
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def task_basic_func(in_data):
    print(f"The digit sum of {in_data} is {digitSum(in_data)}.")
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#----------------------------------------------------------------------
def digitSum(num):
    num = list(filter(lambda x: isdigit(x), num))
    print(num)
    sum = 0
    for i in range(len(num)):
        sum += int(num[i])
    return sum

