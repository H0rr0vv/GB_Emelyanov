def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    print(summa)

n = int(input()) # 5
sumNumbers(n) # 15