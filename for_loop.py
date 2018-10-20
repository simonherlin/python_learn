"""
    for loops
"""
# Looping lists
my_list = [1, 2, 3, 4, 'Python', 'is', 'neat']
for item in my_list:
    print(item)

# break
for item in my_list:
    if item == 'Python':
        break
    print(item)

# continu
for item in my_list:
    if item == 1:
        continue
    print(item)

# enumerate()
for idx, val in enumerate(my_list):
    print('idx: {}, value: {}'.format(idx, val))

# Looping dictionaries
my_dict = {'hacker': True, 'age': 72, 'name': 'John Doe'}
for val in my_dict:
    print(val)
for key, val in my_dict.items():
    print('{}={}'.format(key, val))

# range()
for number in range(5):
    print(number)
for number in range(2, 5):
    print(number)
for number in range(0, 10, 2):  # last one is step
    print(number)
    