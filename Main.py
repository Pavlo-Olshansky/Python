import os

location_of_file = 'D:'
file_name = 'file.txt'

with open(os.path.join(location_of_file, file_name), 'r') as f:
    print(f.read())

who = 'Gary'
how_many = 12
# Gary bought 12 apples today!
print('{0} bought {1} apples today!'.format(who, how_many))
input()
