'''
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
'''

num = int(input('введите число: '))
i = int(0)

while 2 ** i <= num:
    print(f'{2 ** i}, ', end = '')
    i += 1