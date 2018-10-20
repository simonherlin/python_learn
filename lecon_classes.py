"""
    Classe
"""

class MyFirstClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print('Hello {}!'.format(self.name))

my_instance = MyFirstClass('John Doe')
print('my_instance: {}'.format(my_instance))
print('type: {}'.format(type(my_instance)))
print('my_instance.name: {}'.format(my_instance.name))

# methods
alice = MyFirstClass(name='Alice')
alice.greet()

# __init__
class Example:
    def __init__(self):
        print('Now we are inside __init__')
        
print('creating instance of Example')
example = Example()
print('instance created')

class Example:
    def __init__(self, var1, var2):
        self.first_var = var1
        self.second_var = var2
        
    def print_variables(self):
        print('{} {}'.format(self.first_var, self.second_var))
        
e = Example('abc', 123)
e.print_variables()

# __str__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return 'Person: {}'.format(self.name)
    
jack = Person('Jack', 82)
print('This is the string presentation of jack: {}'.format(jack))

# Class variables vs instance variables
class Example:
    # These are class variables
    name = 'Example class'
    description = 'Just an example of a simple class'

    def __init__(self, var1):
        # This is an instance variable
        self.instance_variable = var1

    def show_info(self):
        info = 'instance_variable: {}, name: {}, description: {}'.format(
            self.instance_variable, Example.name, Example.description)
        print(info)


inst1 = Example('foo')
inst2 = Example('bar')

# name and description have identical values between instances
assert inst1.name == inst2.name == Example.name
assert inst1.description == inst2.description == Example.description

# If you change the value of a class variable, it's changed across all instances
Example.name = 'Modified name'
inst1.show_info()
inst2.show_info()

# Public vs private
class Person:
    def __init__(self, age):
        self._age = age
        
example_person = Person(age=15)
# You can't do this:
# print(example_person.age)
# Nor this:
# example_person.age = 16

class Person:
    def __init__(self, age):
        self._age = age
        
    @property
    def age(self):
        return self._age
    
    def celebrate_birthday(self):
        self._age += 1
        print('Happy bday for {} years old!'.format(self._age))
        
example_person = Person(age=15)
example_person.celebrate_birthday()

# Introduction to inheritance
class Animal:
    def greet(self):
        print('Hello, I am an animal')

    @property
    def favorite_food(self):
        return 'beef'


class Dog(Animal):
    def greet(self):
        print('wof wof')


class Cat(Animal):
    @property
    def favorite_food(self):
        return 'fish'

dog = Dog()
dog.greet()
print("Dog's favorite food is {}".format(dog.favorite_food))

cat = Cat()
cat.greet()
print("Cat's favorite food is {}".format(cat.favorite_food))