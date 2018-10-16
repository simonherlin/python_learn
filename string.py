my_string = 'Python is my favorite programming language!'
print (my_string)
# respect of the pep8
long_story = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
              'Pellentesque eget tincidunt felis. Ut ac vestibulum est.'
              'In sed ipsum sit amet sapien scelerisque bibendum. Sed '
              'sagittis purus eu diam fermentum pellentesque.')
#str.replace
# This will not modify my_string because replace is not done in-place.
my_string.replace('a', '?')
print(my_string)
# You have to store the return value of replace instead
my_modified_string = my_string.replace('is', 'will be')
print(my_modified_string)
# str.format
secret = '{} is cool'.format('Python')
print(secret)
print('My name is {} {}, you can call me {}.'.format('John', 'Doe', 'John'))
# is the same as:
print('My name is {first} {family}, you can call me {first}.'
    .format(first='John', family='Doe'))
