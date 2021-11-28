# None Primitive dataType
#1- list data type
# homogeneous list
items = [1, 2, 3, 4, 5]
items.clear() # Remove all items in the list
r_item = items.pop(3) # pop removes the item and returns it
print(f'item removed in the list is {r_item}')
items.remove(5) # Remove removes specified value
print(items)
print(type(items))
# heterogeneous
items_2 = [1, 'text', True, -2, .1]
items.append(items_2) # append takes 1 argument to be added in the list
items.append(45)
items.append([0, 1, 2])
print(items)
print(len(items))
i = items.index([0, 1, 2], 0, 7) # index finds the index of given value that exist in the list
print(i)
c = items.copy() # copy copies the original list
print(c*2 < items)
print(c)
#2- tuple data type
#3- dictionary data type
#4- set data type