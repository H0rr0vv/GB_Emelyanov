# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? 
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

n = int(input('Столько километров машина проезжает за день: '))

m = int(input('Столько нужно проехать: '))

t = m // n + (m % n > 0)

print(t)