'''
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

*Пример:*

**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
    **Вывод:** Парам пам-пам  
'''


def beat_check(poem) -> bool:
    val_a = [0]
    for i in range(len(poem)):
        if poem[i] == ' ':
            val_a.append(0)
    i = 0
    for j in range(len(poem)):
        if poem[j] == 'а':
            val_a[i] += 1
        elif poem[j] == ' ':
            i += 1           
    if len(set(val_a)) == 1:
        return True
    return False



poem_winny = input('Введите стих: ')
print(poem_winny)
poem_winny = list(poem_winny)


print('Парам пам-пам') if beat_check(poem_winny) == True else print('Пам парам')

