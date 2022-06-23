# Чтение кода - это и есть основа программирования!


































"""
# логические операторы: and, or, not
"""

"""
# Вычисляем любую цифру числа.
n = 1234        # четырехзначное число
p = 1000        #         1000

print(n // p)   # 1
n = n % p       #    234
p = p // 10     #         100

print(n // p)   # 2
n = n % p       #    34
p = p // 10     #         10

print(n // p)   # 3
n = n % p       #    4
p = p // 10     #         1

print(n // p)   # 4

# Разбор
num = int(input())            # берем 5-ти значимое число к примеру "45826"
digit1 = num // 10 ** 4            # получаем 1-е число "4"
digit2 = (num // 10 ** 3) % 10     # получаем 2-е число "5"
digit3 = (num // 10 ** 2) % 10     # получаем 3-е число "8"
digit4 = (num // 10) % 10          # получаем 4-е число "2"
digit5 = num % 10                  # получаем 5-е число "6"
print(digit1, digit2, digit3, digit4, digit5,  sep='_')
"""


"""
age = int(input('How old are you?'))
if not age < 12:
  print('Access is allowed.')
else:
  print('Access denied.')
"""
  
"""
age = int(input('How old are you?'))
grade = int(input('which class are you in?'))
city = input('What city do you live in?')
if age >= 12 and grade >= 7 and (city == 'Moskov' or city == 'Saint-Petersberg'):
  print('Access is allowed.')
else:
  print('Access denied.')
"""

"""
age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))
city = input('В каком городе вы живете?: ')
if age >= 12 and grade >= 7 and city == 'Москва':
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')
"""
"""
city = input('В каком городе вы живете?: ')
if city == 'Москва' or city == 'Санкт-Петербург' or city == 'Екатеринбург':
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')

"""



"""
age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))
if age >= 12 and grade >= 7:
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')
"""


"""

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
  
"""