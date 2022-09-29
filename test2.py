# dir() - возвращает методы обьекта или функции определенного модуля

# Import match
# print (dir(math))


# """
# множественное присваивание 
# """

# a = 5
# a, b, c, = 1, 2, 3
# v =5
# n = 7
# d = 3
# v, n, d = d, v, n
# print (v, n, d)

# num1 = 10
# num2 = 3
# num3 = num1
# num1 = num2
# num2 = num3
# print (num1, num2)

# print ('hello' *3)


# str1 = '12'
# num1 = 2
# print (str1 + str(num1))
# инкремент - увелеичение значение какой либо переменной. пример; (a = 1 (a += 1 -> a = a + 1))

# a = 12
# a += 11
# print (a)


# дикремент - уменьшение значение какой-либо переменной. (a -= -> a = a - 1)

# a = 0
# a -= 1
# print (a)

# *
# a = 5
# a *= a
# print (a)

# /
# a = 10
# a /= 2
# print (a) 

# id () -> ноиер в ячейке памяти

a = 1
a = 1
print (id (a))


# type (-> выводит тип заданной перемонной)
# a = 9
# b = 'hello'
# print (type(a))
# print (type(b))

# num1 = int(input('ведите число:'))
# num2 = int(input('ведите степень:'))
# print (num1**num2)

# модуль рандом - предоставляет функции для генерации случайных чисел, буквы, символы

# import random
# print (dir(random))
# num = random.randint(11111, 99999)
# print(num)


# from random import choice
# import string 
# # print (string.ascii_letters)

# a = choice(string.ascii_letters)
# print(a)



# периметр 2 * r * pi
# площадь pi * (r**2)


from math import pi

r = int(input('ведите радиус: '))
result_P = 2 * r *pi 
result_S = pi * (r **  2)
print ('площадь окружности \n', round(result_S))
print ('периметр окружности', round(result_P))



# import math
# # r = float (input («Пожалуйста, введите радиус круга r:»))

#  p = 2 * math.pi * r # периметр круга
#  S = mat.pi * r ** 2 # площадь круга
#  печать («Окружность круга есть:», стр.)
#  print («Площадь круга:», с)
