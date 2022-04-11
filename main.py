# choice between two values
# Write a program that reads one line

word = input()
if word == 'Python':
    print('ДА')
else:
    print('НЕТ')


# Write a program that determines whether a two-digit number entered from the keyboard consists of identical digits

num = int(input())
last_digit = num % 10    # последняя цифра числа
first_digit = num // 10  # первая цифра числа

if last_digit == first_digit:
    print('ДА')
else:
    print('НЕТ')


# Write a program that reads three numbers and counts the number of even numbers

num1, num2, num3 = int(input()), int(input()), int(input())
counter = 0  # переменная счётчик
if num1 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num2 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
if num3 % 2 == 0:
    counter = counter + 1  # увеличиваем счётчик на 1
print(counter)

# Code samples
# 1

a = input()
b = input()

if a == b:
    print('Пароль принят')
else:
    print('Пароль не принят')

# 2

i = int(input())
if i % 2 == 0:
    print('Четное')
else:
    print('Нечетное')

# 3

num = int(input())

d = num % 10
c = (num % 100) // 10
b = (num // 100) % 10
a = num // 1000

if a + d == b - c:
    print('ДА')
else:
    print('НЕТ')

# 4

age = int(input())

if age >= 18:
    print('Доступ разрешен')
else:
    print('Доступ запрещен')

# 5

a = int(input())
b = int(input())
c = int(input())

if ((b - a) == (c - b)):
    print('YES')
else:
    print('NO')

# 6

a = int(input())
b = int(input())

if a > b:
    print(b)
else:
    print(a)

# 7

a, b, c, d = int(input()), int(input()), int(input()), int(input())

if a > b:
    a = b

if c > d:
    c = d

if a > c:
    print(c)
else:
    print(a)

# 8

a = int(input())

if a <= 13:
    print('детство')

if 14 <= a < 24:
    print('молодость')

if 25 <= a < 59:
    print('зрелость')

if (a >= 60):
    print('старость')

# 9

a, b, c = int(input()), int(input()), int(input())

d = 0

if a > 0:
    d = d + a
if b > 0:
    d = d + b
if c > 0:
    d = d + c
print(d)
  
