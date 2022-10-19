# 1 - Define the id of variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

list_var = [int_a, str_b, set_c, lst_d, dict_e]
for i in list_var:
    print(id(i))
#
#2. Appending 4 and 5 to the lst_d and define the id one more time:
lst_d.append(4)
lst_d.append(5)
print('\n#2:', lst_d, '- id:', id(lst_d))
#
# 3. Defining the type of each object from step 1:
print('\n#3:')
for i in list_var:
    print(type(i))
#
# # 4*. Check the type of the objects by using isinstance:
print('\n#4:', isinstance(int_a,float))
print('\t', isinstance(str_b,str))
print('\t', isinstance(set_c,set))
print('\t', isinstance(lst_d,list))
print('\t', isinstance(dict_e,dict))

# # String formatting:
# # Replace the placeholders with a value:
# # "Anna has ___ apples and ___ peaches."
#
# # 5. With .format and curly braces {}
print('\n#5:', 'Anna has {} apples and {} peaches'. format(2, 4))
#
# 6. By passing index numbers into the curly braces.
print('\n#6:', 'Anna has {1} apples and {0} peaches'. format(2, 4))
#
# 7. By using keyword arguments into the curly braces.
print('\n#7:', 'Anna has {apple} apples and {peach} peaches'. format(apple=3, peach=4))
#
# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print('\n#8:''Anna has {0:_^5s} apples and {1:_>3d} peaches'. format('three', 70))
#
# # 9. With f-strings and variables
apl = 6
pea = 7
print('\n#9:', f'Anna has {apl} apples and {pea} peaches')
#
# # 10. With % operator
print('\n#10:', 'nAna has %d apples and %d peaches' % (apl, pea))
#
# # 11*. With variable substitutions by name (hint: by using dict)
diction = {'apple': 17, 'peach': 18}
print('\n#11:', f"Anna has {diction['apple']} apples and {diction['peach']} peaches")
# var1="three"
# var2="one thousand"
# data_dict={"one": var1, "two": var2}
# print('Anna has %(one)s apples and %(two)s peaches.' % data_dict)
# Comprehensions:
# (1)
# lst = []
# for num in range(10):
#     if num % 2 == 1:
#         lst.append(num ** 2)
#     else:
#         lst.append(num ** 4)
# print(lst)
#
# (2)
# list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
# print(list_comprehension)
#
# 12. Convert (1) to list comprehension
list_compr12 = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print('\n#12:', list_compr12)
# 13. Convert (2) to regular for with if-else
list_compr13 = []
for numb in range(10):
    if numb % 2 == 0:
        list_compr13.append(numb // 2)
    else:
        list_compr13.append(numb * 10)
print('\n#13:', list_compr13)
#
# (3)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
# print(d)
#
#
# (4)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
#     else:
#         d[num] = num // 0.5
# print(d)
#
#
# (5)
# dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
#
#
# (6)
# dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
#
#
# 14. Convert (3) to dict comprehension.
dict_compr = {number: number ** 2 for number in range(1, 11) if number % 2 == 1}
print('\n#14:', dict_compr)
# 15*. Convert (4) to dict comprehension.
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
#     else:
#         d[num] = num // 0.5
# print(d)
dict_compr2 = {numer: numer ** 2 if numer % 2 == 1 else numer // 0.5 for numer in range(1, 11)}
print('\n#15:', dict_compr2)

# 16. Convert (5) to regular for with if.
# dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
# print(dict_comprehension)

dict_compr3 = {}
for x in range(10):
    if x**3 % 4 == 0:
        dict_compr3[x] = x**3
print('\n#16:', dict_compr3)

# 17*. Convert (6) to regular for with if-else.
# dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
# print(dict_comprehension)

dict_compr4 = {}
for x in range(10):
    if x**3 % 4 == 0:
        dict_compr4[x] = x**3
    else:
        dict_compr4[x] = x
print('\n#17:', dict_compr4)

# Lambda:
#
# (7)
# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y
#
# (8)
# foo = lambda x, y, z: z if y < x and x > z else y
#
#
# 18. Convert (7) to lambda function
lambd_func = lambda x, y: x if x < y else y
print('\n#18:', lambd_func(6, 5))
# 19*. Convert (8) to regular function
def regular_f(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y
print('\n#19:', regular_f(1, 10, 4))


lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
# 20. Sort lst_to_sort from min to max
print('\n#20:', sorted(lst_to_sort))
# 21. Sort lst_to_sort from max to min
print('\n#21:', sorted(lst_to_sort, reverse=True))
# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
lst_2 = list(map(lambda i: i*2, lst_to_sort))
print('\n#22:', lst_2)
# 23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]
lst_3 = list(map(lambda y: y+3, list_A))
print('\n#23:', lst_3)
# 24. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
filtr = list(filter(lambda n: n % 2 == 1, lst_to_sort))
print('\n#24:', filtr)
# 25. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
filtr2 = list(filter(lambda n: n < 0, range(-10, 10)))
print('\n#25:', filtr2)
# 26*. Using the filter function, find the values that are common to the two lists:
list_126 = [1,2,3,5,7]
list_226 = [2,3,5,6,7]
filtr3 = list(filter(lambda k: k in list_126, list_226))
print('\n#26:', filtr3)

