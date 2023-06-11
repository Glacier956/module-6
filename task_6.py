print('Задача 6. Вклады')

# Вклад в банке составляет X рублей.
# Ежегодно он увеличивается на P процентов,
# после чего дробная часть копеек отбрасывается.

# Определите, через сколько лет вклад составит не менее Y рублей.

# Напишите программу,
# которая по данным числам X, Y, P определяет,
# сколько лет пройдёт, прежде чем сумма достигнет значения Y.

years = 0

x = int(input("Введите сумму вклада: "))
p = int(input("Введите процент: "))
y = int(input("Введите сумму цели: "))

while x < y: 
  x *= 1 + p / 100 
  x = int(100 * x) / 100 
  years += 1 
print("Пройдёт", years, "лет.")