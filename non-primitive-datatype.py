# None Primitive dataType
#1- list data type
# homogeneous list
items = [1, 2, 3, 4, 5, 5, 7, 77, 77, 9, 9, 9, False, False, False, 'apples', 'apples', 'orange', 'orange']
# items.clear() # Remove all items in the list
# r_item = items.pop(3) # pop removes the item and returns it
# print(f'item removed in the list is {r_item}')
# items.remove(5) # Remove removes specified value
print(items)
print(type(items))
# heterogeneous
items_2 = [1, 'text', True, -2, .1]
items.append(items_2) # append takes 1 argument to be added in the list
items.append(45)
items.append([0, 1, 2])
items.append([3, 4, 5, [-1, -2, -3]])
print(items)
print(len(items))
# i = items.index([0, 1, 2], 0, 7) # index finds the index of given value that exist in the list
# print(i)
c = items.copy() # copy copies the original list
print(c*2 < items)
print(c)
apples = items.count('apples')
print(apples)
num_9 = items.count(9)
print(num_9)
false = items.count(False)
print(false)
ex_items = [1, 2, 3, 4]
items.extend(ex_items)
print(items)
items.insert(5, ex_items)
print(items)
items.reverse()
print(items)
nums = [5, 4, 3, 2, 1, 0]
# nums.sort(reverse=False)
# print(nums)
n = sorted(nums, reverse=False)
print(n)
# print(help(sorted))
a = items[4:5]
print(a)
a = items[4:5][0][3][0]
print(a)
data = 'i want to eat apples'

d = data.split()
print(d[1::-2])
email = 'my email address is john.doe@gmail.com'
e = email.split()[4]
print(e.split('@')[0][0:4])

# Homework
#Task 1
"""
1- initialize an empty list.
2- add person's info to the list such first name, last name, age, position, an email address and etc.
Hint! a) the person's info must be entered dynamically. b) person's email must be an instance of first and last name.
"""
# Task 2
"""
1- Make static list that has the same info like above but different info.
2- Extend the 2nd list to the first list
3- Print out each person first name as username, age, an email with the message.
---------------------------------------------------------------------------------
Good luck 👍 😃 :)
"""
#2- tuple data type
#3- dictionary data type
#4- set data type