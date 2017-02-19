example = ['left', 'right', 'up', 'down']

for i, j in enumerate(example):
    print(i+1, j)

new_dict = dict(enumerate(example))
print('Dict :', new_dict)

[print(i, j) for i, j in enumerate(example)]

print('------------------- 8 ------------------')

x = [1, 2, 3, 4]
y = [7, 6, 4, 8]
z = ['a', 'b', 'c', 'd']

# for a, b, c in zip(x, y, z):
#     print(a, b, c)


# print(zip(x, y ,z))  # generator
#
# [print(i) for i in zip(x, y, z)]
# my_list = [print(list(zip(x, z, y)))]
# my_dict = [print(dict(zip(x, y)))]
#
# [print(a, b, c) for a, b, c in zip(x, y, z)]  # -- temporary variable
# print(a)
#
# for a, b in zip(x, y):  # value a - is stored
#     print(a, b)
# print('This is a now :', a)

for x, y in zip(x, y):  # value a - is stored
    print(x, y)
print('This is X now :', x)
