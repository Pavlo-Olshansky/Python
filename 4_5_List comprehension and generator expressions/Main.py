xyz = [i for i in range(5)]

print(xyz)

xyz = (i for i in range(5))  # generator - it's in your memory now
print(xyz)
for i in xyz:
    print(i)

# Generator's faster creating, but for working with them - it's longer
print('-------- 5 ----------\n')

input_list = [1, 5, 7, 10, 3, 20, 25, 12, 5]


def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

xyz = (i for i in input_list if div_by_five(i))  # We sabing a memory, but it's slower
[print(i) for i in xyz]

xyz = [i for i in input_list if div_by_five(i)]  # We don't sabing a memory, but it's faster
[print(i, end=' ') for i in xyz]

[[print(i, ii) for ii in range(3)] for i in range(3)]

board = ([(i+1, ii+1) for ii in range(555)] for i in range(5))  # Generator with 2 loops - must iterate
[print(i) for i in board]  #like a board
# [[print(ii) for ii in i] for i in board] # in line
