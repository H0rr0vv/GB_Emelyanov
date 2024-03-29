'''
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию
.split()
'''

init_list = list(input('Введите строку: '))

dictionary = {}

for item in init_list:
    dictionary[item] = dictionary.get(item, 0) + 1
    print(item if dictionary.get(item) < 2 else (str(item) + '_' + str(dictionary.get(item) - 1)), end = ' ')