# get - default value of a non existing key while accessing
my_dict = {'a': 1, 'b': 2, 'c': 3}
# bad
if 'g' in my_dict:
    value = my_dict['g']
else:
    value = 'some default value'
print(value)
# bad to
try:
    value = my_dict['g']
except KeyError:
    value = 'some default value'
print(value)
# good
value = my_dict.get('g', 'some default value')
print(value)

# setdefault - same as get but also sets the value if not present
# bad
my_dict = {'a': 1, 'b': 2, 'c': 3}

key = 'g'
if key in my_dict:
    value = my_dict[key]
else:
    value = 'some default value'
    my_dict[key] = value
print(value)
print(my_dict)
# good
my_dict = {'a': 1, 'b': 2, 'c': 3}
key = 'g'
value = my_dict.setdefault(key, 'some default value')
print(value)
print(my_dict)

# Comprehensions
numbers = (1, 5, 10)
# bad
squares = {}
for num in numbers:
    squares[num] = num**2
print(squares)
# good
squares = {num: num**2 for num in numbers}
print(squares)

# Another example
keys = ('a', 'b', 'c')
values = [True, 100, 'John Doe']
# bad
my_dict = {}
for idx, key in enumerate(keys):
    my_dict[key] = values[idx]
print(my_dict)
# good
my_dict = {k: v for k, v in zip(keys, values)}
print(my_dict)
# Or even like this:
my_dict2 = dict(zip(keys, values))
assert my_dict2 == my_dict

# Looping
my_dict = {'age': 83, 'is gangster': True, 'name': 'John Doe'}
# bad
for key in my_dict:
    val = my_dict[key]
    print('key: {:15s} value: {}'.format(key, val))
# good
for key, val in my_dict.items():
    print('key: {:15s} value: {}'.format(key, val))