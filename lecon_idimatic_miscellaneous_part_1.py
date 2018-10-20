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
