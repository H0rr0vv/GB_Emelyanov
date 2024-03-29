'''
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко; 
D, G – 2 очка; 
B, C, M, P – 3 очка; 
F, H, V, W, Y – 4 очка; 
K – 5 очков; 
J, X – 8 очков; 
Q, Z – 10 очков. 


А русские буквы оцениваются так: 
А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
Д, К, Л, М, П, У – 2 очка; 
Б, Г, Ё, Ь, Я – 3 очка; 
Й, Ы – 4 очка; 
Ж, З, Х, Ц, Ч – 5 очков; 
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков. 
Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

*Пример:*

ноутбук
    12
'''

my_word = input(f'Слово: ').lower()
points = int(0)

en_ru_dict = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'l': 1, 'n': 1, 's': 1, 't': 1, 'r': 1, 
                'а': 1, 'в': 1, 'е': 1, 'и': 1, 'н': 1, 'о': 1, 'р': 1, 'с': 1, 'т': 1,
                'd': 2, 'g': 2, 
                'д': 2, 'к': 2, 'л': 2, 'м': 2, 'п': 2, 'у': 2, 
                'b': 3, 'c': 3, 'm': 3, 
                'p': 3, 'б': 3, 'г': 3, 'ё': 3, 'ь': 3, 'я': 3, 
                'f': 4, 'h': 4, 'v': 4, 'w': 4, 
                'y': 4, 'й': 4, 'ы': 4, 
                'k': 5, 
                'ж': 5, 'з': 5, 'х': 5, 'ц': 5, 'ч': 5, 
                'j': 8, 'x': 8, 
                'ш': 8, 'э': 8, 'ю': 8, 
                'q': 10, 'z': 10, 
                'ф': 10, 'щ': 10, 'ъ': 10}

my_word = list(my_word)
count = int(0)

while count < len(my_word):
    points += en_ru_dict[my_word[count]]
    count += 1

print(f'Очков: {points}')