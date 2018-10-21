# String concatenation
names = ('John', 'Lisa', 'Terminator', 'Python')
# bad
semicolon_separated = names[0]
for name in names[1:]:
    semicolon_separated += ';' + name
print(semicolon_separated)
# good
semicolon_separated = ';'.join(names)
print(semicolon_separated)

# or in assignments
a = 0
b = None
c = 'John Doe'
# bad
my_variable = 'default value'
if a:
    my_variable = a
elif b:
    my_variable = b
elif c:
    my_variable = c
print(my_variable)
# good
my_variable = a or b or c or 'default value'
print(my_variable)

# try - except - else
# Don't use the following technique for checking 
# if there was exceptions during execution of some block of code.
exception_occured = False
try:
    # here would be the logic of your master piece
    bad_calculation = 1 / 0
except ValueError as e:
    print('Oh boi, some value error: {}'.format(e))
    exception_occured = True
except Exception as e:
    print('Oh boi, something bad happened: {}'.format(e))
    exception_occured = True
if not exception_occured:
    print('All went well!')
# Use this instead!
try:
    # here would be the logic of your master piece
    bad_calculation = 1 / 0
except ValueError as e:
    print('Oh boi, some keyerror: {}'.format(e))
except Exception as e:
    print('Oh boi, something bad happened: {}'.format(e))
else:
    print('All went well!')

# try - finally
# bad
def magical_calculation():
    try:
        # here would be the logic of your master piece
        result = 1 / 0
    except ZeroDivisionError:
        print('This could be something important that should be done every time')
        return 0
    except Exception:
        print('This could be something important that should be done every time')
        return None
    print('This could be something important that should be done every time')
    return result
print('return value: {}'.format(magical_calculation()))
# This is better fit for the purpose!
def magical_calculation():
    try:
        # here would be the logic of your master piece
        result = 1 / 0
    except ZeroDivisionError:
        return 0
    except Exception:
        return None
    finally:
        print('This could be something important that should be done every time')
    return result
print('return value: {}'.format(magical_calculation()))

# Use context managers when possible
# bad
try:
    some_file = open('tmp.txt', 'w')
    print('the file is now open: {}'.format(not some_file.closed))
    # here would be some logic
finally:
    some_file.close()
    print("now it's closed: {}".format(some_file.closed))
# good
with open('tmp.txt', 'w') as some_file:
    print('the file is now open: {}'.format(not some_file.closed))
    # here would be some logic
print("now it's closed: {}".format(some_file.closed))
# It's also easy to implement one yourself.
from contextlib import contextmanager
@contextmanager
def my_context():
    print('Entering to my context')
    yield
    print('Exiting my context')
def do_stuff():
    with my_context():
        print('Doing stuff')
    print('Doing some stuff outside my context')
do_stuff()  

# min() & max()
secret_data = (1, 2, 5, 99, 8, -9)
# bad
max_value = 0
for val in secret_data:
    if val > max_value:
        max_value = val
print(max_value)
# good
max_value = max(secret_data)
print(max_value)

# contextlib.suppress - ignoring exceptions
# bad
value = 0
try:
    value = 1 / 0  # just for demonstrating purposes 
except ZeroDivisionError:
    pass
print(value)
# good
from contextlib import suppress
value = 0
with suppress(ZeroDivisionError):
    value = 1 / 0  # just for demonstrating purposes
print(value)

# Properties instead of getter/setter methods
# bad 
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name        
    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    def set_full_name(self, full_name):
        parts = full_name.split()
        if len(parts) != 2:
            raise ValueError('Sorry, too difficult name')
        self.first_name, self.last_name = parts 
p = Person('John', 'Doe')
print(p.get_full_name())
p.set_full_name('Lisa Doe')
print(p.get_full_name())

class Person2:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    @full_name.setter
    def full_name(self, name):
        parts = name.split()
        if len(parts) != 2:
            raise ValueError('Sorry, too difficult name')
        self.first_name, self.last_name = parts
p = Person2('John', 'Doe')
print(p.full_name)
p.full_name = 'Lisa Doe'
print(p.full_name)