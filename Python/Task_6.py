'''
Задача 6: Вы пользуетесь общественным транспортом? 
Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no
'''

ticket = str(input('Вам попался билет: '))

val1 = ticket[0]
val1 = int(val1)

val2 = ticket[1]
val2 = int(val2)

val3 = ticket[2]
val3 = int(val3)

val4 = ticket[3]
val4 = int(val4)

val5 = ticket[4]
val5 = int(val5)

val6 = ticket[5]
val6 = int(val6)

if val1 + val2 + val3 == val4 + val5 + val6:
    print(f'{ticket} -> yes')
else:
    print(f'{ticket} -> no')