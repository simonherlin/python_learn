"""
    testing truth value
"""
# bool
print('type of True and False: {}'.format(type(True)))
print('0: {}, 1: {}'.format(bool(0), bool(1)))
print('empty list: {}, list with values: {}'.format(bool([]), bool(['woop'])))
print('empty dict: {}, dict with values: {}'.format(bool({}), bool({'Python': 'cool'})))
# ==, !=, >, <, >=, <=
print('1 == 0: {}'.format(1 == 0))
print('1 != 0: {}'.format(1 != 0))
print('1 > 0: {}'.format(1 > 0))
print('1 > 1: {}'.format(1 > 1))
print('1 < 0: {}'.format(1 < 0))
print('1 < 1: {}'.format(1 < 1))
print('1 >= 0: {}'.format(1 >= 0))
print('1 >= 1: {}'.format(1 >= 1))
print('1 <= 0: {}'.format(1 <= 0))
print('1 <= 1: {}'.format(1 <= 1))
print('1 <= 2 <= 3: {}'.format(1 <= 2 <= 3))
# and, or, not
python_is_cool = True
java_is_cool = False
empty_list = []
secret_value = 3.14
print('Python and java are both cool: {}'.format(python_is_cool and java_is_cool))
print('secret_value and python_is_cool: {}'.format(secret_value and python_is_cool))
print('Python or java is cool: {}'.format(python_is_cool or java_is_cool))
print('1 >= 1.1 or 2 < float("1.4"): {}'.format(1 >= 1.1 or 2 < float('1.4')))
print('Java is not cool: {}'.format(not java_is_cool))
print(bool(not java_is_cool or secret_value and  python_is_cool or empty_list))
print(bool(not (java_is_cool or secret_value and  python_is_cool or empty_list)))
