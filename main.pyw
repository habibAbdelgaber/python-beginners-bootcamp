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

print('---------------------------------------------------------------------------------')

# variable/s or container
f_name = 'John'
s_name = 'Jackson'
_name = 'Aziz'

print('my name is: ', f_name, s_name, _name)

# practice
# 1- say something as greeting message  and assign to variable
msg = 'Hi there'
# 2- assign two vars to first name and second name to two person
f_name_1 = 'John'
s_name_1 = 'Doe'

f_name_2 = 'Alberto'
s_name_2 = 'Carlos'

# 3- assign each person's first and second name to full name variable
fullname_1 = f_name_1 + ' ' + s_name_1
fullname_2 = f_name_2 + ' ' + s_name_2
# 4- print them out
print(msg, fullname_1)
print(msg, fullname_2)
print('------------------------------------')
# what is input function or method
print(input)
print(input('what is your name? '), input('and i am: '))
name = input('what is your name? ')
print(name)
# 1- Assign person with first, last name and age using input built-in function
person_name_1 = input('What is your first name? ')
person_name_2 = input('What is your last name? ')
born = int(input('when you were born? '))
current_year = int(input('what is current year? '))
age = eval(input('how old are you? '))
print(type(age))
person_age = int(input('How old are you? '))
print(type(person_age))
# 2- assign full name var to first, last name and
fullname = person_name_1 + ' ' + person_name_2 + ' ', person_age
fullname = person_name_1 + ' ' + person_name_2 + ' ', current_year - born
fullname = person_name_1 + ' ' + person_name_2 + ' ', age
# 3- print out full name's detail
print(fullname)

print('----------------------------------------')
print(format) # format is built-in function
name = 'john'
msg = 'helooo'
# detail = format(msg, name) # in both py2 / py3
detail = f'{msg} i am {name}' # f string new in py3
print(detail)

# Built-in methods
name = 'Horress'.lower()
print(name)
upper_name = name.upper()
print(upper_name)
capitalize_name = name.capitalize()
print(capitalize_name)

# Homework assignment
# 1- assign Adam, Idris and 44 to vars / variables and print it out
"""
2- ask a user to enter his/her first, last, password including age in the prompt #Hint use input built-in function.
a) print out user's fullname.
b) assign email var to user's first and last as valid email address. Hint! don't forget this: @gmail.com using Fstring format.
c) make a password unreadable string or hash password.
d) print out user first name, last name, password and email address with name their keys for e.g First name = first_name using Fstring format.
"""






