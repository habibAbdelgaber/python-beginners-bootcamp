# # variable/s or container
# f_name = 'John'
# s_name = 'Jackson'
# _name = 'Aziz'
#
# print('my name is: ', f_name, s_name, _name)
#
# # practice
# # 1- say something as greeting message  and assign to variable
# msg = 'Hi there'
# # 2- assign two vars to first name and second name to two person
# f_name_1 = 'John'
# s_name_1 = 'Doe'
#
# f_name_2 = 'Alberto'
# s_name_2 = 'Carlos'
#
# # 3- assign each person's first and second name to full name variable
# fullname_1 = f_name_1 + ' ' + s_name_1
# fullname_2 = f_name_2 + ' ' + s_name_2
# # 4- print them out
# print(msg, fullname_1)
# print(msg, fullname_2)
# print('------------------------------------')
# # what is input function or method
# print(input)
# print(input('what is your name? '), input('and i am: '))
# name = input('what is your name? ')
# print(name)
# # 1- Assign person with first, last name and age using input built-in function
# person_name_1 = input('What is your first name? ')
# person_name_2 = input('What is your last name? ')
# born = int(input('when you were born? '))
# current_year = int(input('what is current year? '))
# age = eval(input('how old are you? '))
# print(type(age))
# person_age = int(input('How old are you? '))
# print(type(person_age))
# # 2- assign full name var to first, last name and
# fullname = person_name_1 + ' ' + person_name_2 + ' ', person_age
# fullname = person_name_1 + ' ' + person_name_2 + ' ', current_year - born
# fullname = person_name_1 + ' ' + person_name_2 + ' ', age
# # 3- print out full name's detail
# print(fullname)
#
# print('----------------------------------------')
# print(format) # format is built-in function
# name = 'john'
# msg = 'helooo'
# # detail = format(msg, name) # in both py2 / py3
# detail = f'{msg} i am {name}' # f string new in py3
# print(detail)
#
# # Built-in methods
# name = 'Horress'.lower()
# print(name)
# upper_name = name.upper()
# print(upper_name)
# capitalize_name = name.capitalize()
# print(capitalize_name)

# Homework assignment
# 1- assign Adam, Idris and 44 to vars / variables and print it out
first_name = 'Adam'
last_name = 'Idris'
age = 44
# print('Hi ', first_name, last_name, 'and i am ', age, ' yrs old!')
# 2- ask a user to enter his/her first, last, password including age in the prompt #Hint use input built-in function.
fname = input('what is your name? ')
lname = input('what is your last name? ')
password = input('enter your password? ')
age = input('how old are you? ? ')
# a) print out user's fullname.
# fullname = fname, lname, password, age
# print(fullname)
# b) assign email var to user's first and last as valid email address. Hint! don't forget this: @gmail.com using
# Fstring format.
email = f'{fname.lower()}.{lname.lower()}@gmail.com'
# print(email)
# c) make a password unreadable string or hash password.
# hash_password = '***' * len(password)
hash_password = password * len(password)
# print('Hashed password: ', hash_password)
# d) print out user first name, last name,
# password and email address with  their keys for e.g First name = first_name using Fstring format.
details = f'Fist name: {fname} Last name: {lname} Age: {age} Email address: {email} Password: {hash_password}'
details = f'Hi, i am {fname} {lname} and i am\t{age} yrs old!\n\ne-mail address is: {email}\n\nIt\'s Password: {hash_password}'
print(details)