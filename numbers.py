# int
my_int = 6
print('value: {}, type: {}'.format(my_int, type(my_int)))
# float
my_float = float(my_int)
print('value: {}, type: {}'.format(my_float, type(my_float)))

# Note that division of ints produces float
print(1 / 1)
print(6 / 5)

# Be aware of the binary floating-point pitfalls
val = 0.1 + 0.1 + 0.1
print(val == 0.3)
print(val)

# Floor division //, modulus %, power **
print(7 // 5)
print(7 % 5)
print(7 ** 5)
