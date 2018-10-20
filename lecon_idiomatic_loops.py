# Looping in general
data = ['John', 'Doe', 'was', 'here']
# Don't do it like this. While loops are actually really rarely needed.
idx = 0
while idx < len(data):
    print(data[idx])
    idx += 1
# Don't do like this either.
for idx in range(len(data)):
    print(data[idx])

# DO IT LIKE THIS !
for item in data:
    print(item)
# If you need the index as well, you can use enumerate.
for idx, val in enumerate(data):
    print('{}: {}'.format(idx, val))

# Looping over a range of numbers
# Don't do this.
i = 0
while i < 6:
    print(i)
    i += 1
# Don't do this either.
for val in [0, 1, 2, 3, 4, 5]:
    print(val)
# Do it like this!
for val in range(6):
    print(val)

# Reversed looping
data = ['first', 'to', 'last', 'from'] 
# This is no good.
i = len(data) - 1
while i >= 0:
    print(data[i])
    i -= 1
# Do it like this!
for item in reversed(data):
    print(item)

# Looping over n collections simultaneously
collection1 = ['a', 'b', 'c']
collection2 = (10, 20, 30, 40, 50)
collection3 = ['John', 'Doe', True]

# very  bad
shortest = len(collection1)
if len(collection2) < shortest:
    shortest = len(collection2)
if len(collection3) < shortest:
    shortest = len(collection3)
    
i = 0
while i < shortest:
    print(collection1[i], collection2[i], collection3[i])
    i += 1
# bad
shortest = min(len(collection1), len(collection2), len(collection3))
for i in range(shortest):
    print(collection1[i], collection2[i], collection3[i])
# good
for first, second, third in zip(collection1, collection2, collection3):
    print(first, second, third)
#good to for two
my_dict = dict(zip(collection1, collection2))
print(my_dict)

# for - else - Checking for a match in a collection
data = [1, 2, 3, 'This', 'is', 'just', 'a', 'random', 'Python', 'list']
# Bad
found = False
for val in data:
    if str(val).lower() == 'python':
        found = True
        break
if not found:
    raise ValueError("Nope, couldn't find.")
# good
for val in data:
    if str(val).lower() == 'python':
        break
else:
    raise ValueError("Nope, couldn't find.")