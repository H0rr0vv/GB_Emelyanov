# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

S = int(input('Общее количество журавликов: '))

petya = int(0)

serega = int(0)

katya = int(0)

flag = True

while flag:
    if petya + serega + katya == S:
        flag = False
        print(f'{S} -> {petya} {katya} {serega}')
    elif petya + serega + katya > S:
        flag = False
        print('Неправильно заданы условия задачи')
    else:
        petya += 1
        serega += 1
        katya = (petya + serega) * 2
