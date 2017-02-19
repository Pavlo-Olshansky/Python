import timeit


print(timeit.timeit('''
def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

input_list = [i for i in range(100)]
xyz = [i for i in input_list if div_by_five(i)]
for i in xyz:
    x = i
''', number=5000))
# Generators - 0.19197142109088708 ( with print 0.3948744923122583 ) ## - in most casas - faster
# [ ] - 0.37826222160469497 ( 0.3825548236597374 )
# list(()) -0.434391195321664 (0.4145047699254147 )

