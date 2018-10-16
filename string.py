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

# str.join()
pandas = 'pandas'
numpy = 'numpy'
requests = 'requests'
cool_python_libs = ', '.join([pandas, numpy, requests])
print('Some cool python libraries: {}'.format(cool_python_libs))

# alternative but not Pythonic and slower
cool_python_libs = pandas + ', ' + numpy + ', ' + requests
print('Some cool python libraries: {}'.format(cool_python_libs))
cool_python_libs = pandas
cool_python_libs += ', ' + numpy
cool_python_libs += ', ' + requests
print('Some cool python libraries: {}'.format(cool_python_libs))

# str.upper(), str.lower(), str.title()
mixed_case = 'PyTHoN hackER'
print(mixed_case.upper())
print(mixed_case.lower())
print(mixed_case.title())

# str.strip()
ugly_formatted = ' \n \t Some story to tell '
stripped = ugly_formatted.strip()
print('ugly: {}'.format(ugly_formatted))
print('stripped: {}'.format(ugly_formatted.strip()))

# str.split()
sentence = 'three different words'
words = sentence.split()
print(words)
print(type(words))
secret_binary_data = '01001,101101,11100000'
binaries = secret_binary_data.split(',')
print(binaries)
