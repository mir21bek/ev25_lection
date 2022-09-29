# print(dir(str)) #методы строк


# replace(old, new, [count]) - меням в строке old на new значение, если вы укажите ccoount, то он заменит его ровно count раз

# text = 'ha ha ha ha'
# result = text.replace('a', 'i',2) 
# print(f'result after replase:{result}')

# str1 = 'hello world my name is john snow'
# result = str1.replace('john snow', 'jamie lanister')
# print(result)


# print(id('H'))
# print(id('h'))


# strip() - убирает проельные символы в начае и в конце строки
# rstrip, lstrip

# text = input('enter the text: ')
# print(text)
# print(len(text))
# res = text.strip()
# print(res)
# print(len(res))

# text = '   hello world   '
# print(len(text))
# res = text.lstrip()
# print(res)
# print(len(res))


# print(dir(str))

# isdigit ->
# isnumeric -> 
# isdecimal ->
# проверяют состоит ли наша строка полностью из чисел

# text = '57'
# if text.isdigit():
#   num = int(text)
#   print(num)
# else:
#   print('oops invalid symbols')


# text = '\u0030'
# print (text)
# print(text.isnumeric())


# isalnum() -> проверят состоит ли наша строка из чисел и символов латинского алфавита и киррилицы

# str1 = '56a'
# print(str1.isalnum())
# str2 = '56_a'
# print(str2.isalnum())


# isalpha() -> сотоит ли наша строка полностью из символов латинского киррильского алфавита
# text = 'hello world'
# print(text[:5].isalpha())


# islower()
# isupper()
# istitle()

# index(value, [start], [end]) -> выводит индекс значение value которое мы передаем в нашей строке

# count(value, [start]) -> считает количество вхождений value в нащу строки 

# text = 'hello o o world'
# print(text.count('hello'))
# print(text.count('o'))
# print(text.count(' '))

# text = 'hello world! my name is john snow'
# print(text.index('john'))
# res = text.index('o')
# res = text.index('o', res+1)
# print(res)
# print(text[24])

# text ='ooohello world! myo name is john snowooo'
# # text = input('enter the text: ')
# i = 0
# res = -1
# while i <= text.count('o'): #4
#   res = text.index('o', res+1)
#   print(res)
#   i += 1 #инкремент


# find(value, [start], [end]) -> делает тоже самое что и index но есть одно отличие в том если value нет в строке то возвращается индекс -1

# text = 'hello'
# print(text.find('l'))
# print(text.find('hi'))


# swapcase() -> переводит все символы в противоположный регистр
# upper() -> все символы в верхний регистр
# lower() -> все символы в гижний регистр


# text = 'heLLO world, JOhn, SnoW'
# print(text.swapcase())
# print(text.lower())
# print(text.upper())
# print(text)


# capitalize() - переводит первую буквы в верхний регистр

# name = input('enter your name: ').capitalize()
# print(f'hello {name}')

# title() -> переводит первые символы всех слов в первый регистр
# text = 'john jamie sansa nurislam'
# print(text.title())
# print(text.capitalize())
# print(text)

# name = input('ведите ФИО')
# print(name.title())


# split(разделитель) - дробит строку по разделителю который находитсяя в строке все части строки сохраняются в тип данных list
# text = 'let me speak from my hearth in english cause my name is john snow'
# ls = text.split(' ')
# print (ls)
# print(len(ls))


# # 'разделитель'.join(interable(list)) -> соеденяет строки по разделителю строки которые находятся в list

# res = ' '.join(ls)
# print(res)