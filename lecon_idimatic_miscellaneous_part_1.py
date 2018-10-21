# Comprehensions
original_data = (1, 2, 3, 4)
# don't do this
# list
square_roots_list = []
for val in original_data:
    square_root = val**(1/2) 
    square_roots_list.append(square_root)
print(square_roots_list)

# set
square_roots_set = set()
for val in original_data:
    square_root = val**(1/2) 
    square_roots_set.add(square_root)
print(square_roots_set)

# dict
square_roots_dict = {}
for val in original_data:
    square_root = val**(1/2) 
    square_roots_dict[val] = square_root
print(square_roots_dict) 

# dict with a condition
integer_square_roots_dict = {}
for val in original_data:
    square_root = val**(1/2)
    if square_root.is_integer():
        integer_square_roots_dict[val] = square_root
print(integer_square_roots_dict) 

# Use comprehensions!
square_roots_list = [val**(1/2) for val in original_data]
print(square_roots_list)

square_roots_set = {val**(1/2) for val in original_data}
print(square_roots_set)

square_roots_dict = {val: val**(1/2) for val in original_data}
print(square_roots_dict)

integer_square_roots_dict = {
    val: val**(1/2)
    for val in original_data if (val**(1/2)).is_integer()
}
print(integer_square_roots_dict)

# Using in for checking presence of an element in a collection
name = 'John Doe'
# bad
if name == 'John' or name == 'Doe' or name == 'John Doe':
    print('This seems to be our guy')
# good
if name in ('John', 'Doe', 'John

a, b, c, d = 1, 2, 3, 4

 Doe'):
    print('This seems to be our guy')

# Chained comparisons
a, b, c, d = 1, 2, 3, 4
# bad
if b > a and c > b and d > c:
    print('from lowest to highest: a, b, c, d')
# good
if a < b < c < d:
    print('from lowest to highest: a, b, c, d')

# Falsy/truthy values
# These are falsy
my_list = []
my_dict = {}
my_set = set()
my_tuple = tuple()
zero = 0
false = False
none = None
my_str = ''
# Basically the rest are truthy
# for example:
my_second_list = ['foo']
# bad
if len(my_list) == 0:
    print('Empty list is so empty')
if not len(my_dict):
    print('Empty dict is also very empty')
if not len(my_set) and not len(my_tuple):
    print('Same goes for sets and tuples')
if not bool(zero) and not bool(false) and not bool(none) and len(my_str) == 0:
    print('These are also falsy')
if len(my_second_list) > 0:
    print('This should be true')
# good
if not my_list:
    print('Empty list is so empty')    
if not my_dict:
    print('Empty dict is also very empty')
if not my_set and not my_tuple:
    print('Same goes for sets and tuples')
if not zero and not false and not none and not my_str:
    print('These are also falsy')
if my_second_list:
    print('This should be true')

# any & all
example_collection = ['a', True, 'Python is cool', 123, 0]
# bad
any_value_truthy = True
for val in example_collection:
    if val:
        any_value_truthy = True
        break
all_values_truthy = True
for val in example_collection:
    if not val:
        all_values_truthy = False
        break
print('any truthy: {}, all truthy: {}'.format(any_value_truthy, all_values_truthy))
# good
any_value_truthy = any(example_collection)
all_values_truthy = all(example_collection)
print('any truthy: {}, all truthy: {}'.format(any_value_truthy, all_values_truthy))

# Pythonic substitute for ternary operator
"""
    Many other programming languages have a ternary operator: ?. 
    A common use case for the ternary operator 
    is to assign a certain value to a variable based on some condition. 
    In other words, it could be used like this:
        variable = some_condition ? some_value : some_other_value
"""
# Instead of doing this.
some_condition = True  # just a dummy condition
if some_condition:
    variable = 'John'
else:
    variable = 'Doe'
print(variable)
# you can do it like this
variable = 'John' if some_condition else 'Doe'
print(variable)

# Function keywords arguments
def show_person_details(name, is_gangster, is_hacker, age):
    print('name: {}, gangster: {}, hacker: {}, age: {}'.format(
        name, is_gangster, is_hacker, age))
"""
This is not good. It's hard to tell what `True`, `False` and `83` refer here 
if you are not familiar with the signature of the `show_person_details` function
"""
show_person_details('John Doe', True, False, 83)
# This is much better!
show_person_details('John Doe', is_gangster=True, is_hacker=False, age=83)
# Extra: keyword only arguments after `*`
def func_with_loads_of_args(arg1, *, arg2=None, arg3=None, arg4=None, arg5='boom'):
    pass
# This won't work because only keyword arguments allowed after *
#func_with_loads_of_args('John Doe', 1, 2)
# This is ok
func_with_loads_of_args('John Doe', arg4='foo', arg5='bar', arg2='foo bar')

# Multiple assigment
# bad
# original values
a = 1
b = 2
# swap
tmp = a
a = b
b = tmp
print(a, b)
# good
# swap
a, b = b, a
print(a, b)

# (Un)packing
my_list = [1, 2, 3, 4, 5, 6]
# Don't do something like this.
first = my_list[0]
last = my_list[-1]
middle = my_list[1:-1]
print(first, middle, last)
packed = [first] + middle + [last]
assert packed == my_list
# This is the Pythonic way!
# unpacking
first, *middle, last = my_list
print(first, middle, last)
# packing
packed = [first, *middle, last]
assert packed == my_list