"""
    Exception
"""

empty_dict = {}
# empty_dict['key']  # Uncomment to see the traceback

#try-except structure
# Let's try to open a file that does not exist
file_name = 'not_existing.txt'

try:
    with open(file_name, 'r') as my_file:
        print('File is successfully open')
        
except FileNotFoundError as e:
    print('Uups, file: {} not found'.format(file_name))
    print('Exception: {} was raised'.format(e))

def calculate_division(var1, var2):
    result = 0
    
    try:
        result = var1 / var2
    except ZeroDivisionError as ex1:
        print("Can't divide by zero")
    except Exception as ex2:
        print('Exception: {}'.format(ex2))

    return result

result1 = calculate_division(3, 3)
print('result1: {}'.format(result1))

result2 = calculate_division(3, '3')
print('result2: {}'.format(result2))

result3 = calculate_division(3, 0)
print('result3: {}'.format(result3))

def calculate_division(var1, var2):
    return var1 / var2

try:
    result = calculate_division(3, '3')
except Exception as e:
    print(e)

# Creating your custom exceptions
import math

# Define your own exception
class NegativeNumbersNotSupported(Exception):
    pass

# Dummy example how to use your custom exception
def secret_calculation(number1, number2):
    if number1 < 0 or number2 < 0:
        msg = 'Negative number in at least one of the parameters: {}, {}'.format(
            number1, number2)
        raise NegativeNumbersNotSupported(msg)

    return math.sqrt(number1) + math.sqrt(number2)

# Uncomment to see the traceback
# result = secret_calculation(-1, 1)