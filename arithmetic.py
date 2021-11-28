# # other data types --> boolean => bool, None => None
# any = None # => None datatype
# print(any)
# print(type(any))
# print(type(None))
# false = False
# print(false)
# print(type(false))
# print(bool(false))
# print(bool(False))
# print('--------------------------')
# true = True
# print(true)
# print(type(true))
# print(bool(true))
# print(bool(True))
# num1 = 1
# string1 = ''
# print(f'this is {bool(num1)}')
# print(f'this is {bool(string1)}')
# num2 = 0
# string2 = 'test'
# print(f'this is {bool(num2)}')
# print(f'this is {bool(string2)}')
# print(f'this is {bool(None)}')
# # Arithmetic operators --> = assignment, + addition,
# # * multiplication, - subtraction, / division with return of float, // division returns floor.
#
# x = 3
# y = 4
# z = 5
#
# sum = x - y
# c = (x - z ) / y
# x = x - z / y
# print(x)
# print(c)
# print(sum)
#
# # My year income
# budget = 103.3 # USD INVESTED
# daily_income = .05
# yearly_income = f'My Yearly Budget: {12 * 30 * daily_income + budget}'
# print(yearly_income)
#
# investment = 150 # USD
# yrly_income = 500 # YEARLY INCOME
#
# daily_income = f'My Daily income: {yrly_income / investment + investment}'
# print(daily_income)
#
# """
# logical operators:
# 1- < less than
# 2- > greater than
# 3- <= less than or equal to
# 4- >= greater than or equal to
# 5- == equal to
# 6- in value exist into,
# 7- is is the same type
# 8- or is true if one value is true
# 9- and indicates if a and b are true
# 10- != indicates if a and b not true
#
# """
# a = 5
# b = 3
# print(f'is: {a > b}')
# print(f'is: {a <= b}')
#
# num1 = 4
# num2 = 4
# print(f'is: {num2 >= num1}')
# print(f'is: {num2 == num1}')
# print(f'is: {num2 <= num1}')
# print(f'the length of the text is: {num2 <= len("text")}')
# print(f'the length of the text is: {num2 == len("text")}')
#
# str1 = 'hello world'
# str2 = 'hello programmer'
# print(f'is {str1 in str2}')
#
# print(f'hello is in str1 is: {"hello" in str1}')
#
# print(f'the type of str1 is type of str2 is: {type(str1) is type(str2)}')
# print(f'the type of str1 is type of str2 is: {type(str1) is type(len(str2))}')
#
# f = 3
# g = 3
#
# print(f'is: {f == g + f}')
# print(f'is: {f < g + f}')
# print(f'is: {f + g < f}')
#
# a = 4
# b = 4
#
# print(f'is: {a >= b or b + b <= b}')
# print(f'a != b or b != b is: {a != b or b != b}')
# print(f'a == b or b == b is: {a == b or b == b}')
#
# print(f'a != b == b != b is: {a != b == b != b}')
# print(f'a == b and b == b is: {a == b and b == b}')
# print(f'a == b and b => b is: {a == b and b >= b}')
# print(f'(a == b and b <= b) or (a == b and b != b) is: {(a == b and b <= b) or (a == b and b != b)}')
# print(f'(a == b and b <= b) or (a == b and b != b) is: {(a != b and b is b) and (a >= b and b != b)}')

# homework assignment
# Exercise 1
"""
Spent for shopping:
1- consider you bought 5 items
2- the price for each item cost 13.3 USD
3- the tax for 2 items cost .17 cents
a) find the total amount that you're going to pay for your items.
b) find how much taxes you're paid for each item.
"""
items = 5
price = 13.3
taxes = .17
f_two_items = items - 3
taxes_for_all = taxes / f_two_items * items
print(taxes_for_all / items * f_two_items)

total = f"""
I have paid ${items * price}. taxes added {items * price + taxes_for_all}. and total taxes for 5 items {taxes_for_all} and for taxes amount i have paid for two items ${f_two_items * taxes}. and tax for each item {taxes / f_two_items * 1}
"""
print(total)

# Exercise 2
"""
Customer Withdrawing cash from an account:
1- consider a customer has $270 in his/her account.
2- customer has withdrawed some money or all from account dynamically. Hint! use input built-in function.
3- print out how much customer has pulled out from account and how much remains in the account.
"""
# my_current_budget = int(input('My current budget: '))
my_current_budget = 270
customer = int(input('how much you would like to withdraw? '))
withdraw = f'I have pulled out ${customer}, my budget was ${my_current_budget}. And current budget remain ${my_current_budget - customer}'
print(withdraw)
