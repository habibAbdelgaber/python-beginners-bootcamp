# Python bootcamp from zero to hero
print('Hello world')
print(type(print))
print(3 + 3)
print('3' + '3')

# print(Hello' + 'world')
# SyntaxError: invalid syntax

print('Hello' + 'world')
print('Hello' + ' ' + 'world')
print('3' + 'hello')

# print('hello' + 3)
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: can only concatenate str (not "int") to str

print('hello' * 3)
print(3 * 'hello')
print('Habib' + ' ' + 'Abdel' + ' ' + 'Ibrahim')

# print
# File "<stdin>", line 1
# print
# ^
# IndentationError: unexpected indent

print('Hi ' + 'I am ' + 'John Doe ' + 'and ' + 'I am ', 2021 - 1991, 'yrs old!')
print('Hi ' + 'I am ' + 'John Doe ' + 'and ' + 'I am ', 2021 - 1990, 'yrs old!')

print('-------------------------------------------------------------')
# Primitive data types : common primitive data types
# 1- integer (int) positive 12345 or integer negative -12345
# 2- float (float) 21.1656 or float negative -12345.00
# 3- string (str) with length 1


print('the data type is: ', type('text'))
print('the data type is: ', type(12345))
print('the data type is: ', type(11.11))
print('the data type is: ', type(-4j))

# casting or converting
# cast int to float
print(float(10000))

# Homework assignment
# 1- convert str to int or integer
print(len(str(type(int('333')))))  # problem solved
print(len('text'))
# 2- convert int str to integer
print(type(int('55')))
# 3- convert float to int to str
print(type(1.5))
print(type(int(1.5)))
print(type(str(int(1.5))))
print('this data type is: ', type(1.5), 'converted to: ', type(int(1.5)), 'to: ', type(str(int(1.5))))
# 4- find the length and type of 'python programming language' and convert to str or string
print(type(len('python programming language')))
# 5- find the data type of all
# 6- Say Hi, your first and second name, when you were born current year,
# how old are you, how old you will be in 2025 and how many years between your current year and 2025.
print('Hi ', 'i am ' + 'John ' + 'Doe. ' + 'And i am ', 2021 - 1999, 'yrs old ' + 'by the year of ', int('2025'),
      'i will be ', 2021 - 1999 + 2025 - 2021, 'yrs old ' + 'in next ', 2025 - 2021, 'years')







