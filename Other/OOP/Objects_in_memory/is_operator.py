a = [5, 2, 1, 8, 3]
b = [5, 2, 1, 8, 3]

print(a is b)  # False

b = a

print(a is b)  # True

b.append(6)
print(a is b)  # True
print(a, b)  # changed in a and b

a.append(10)
print(a is b)   # True
print(a, b)  # changed in a and b

# a and b even if they are the same list, tuple, set, are not the same object
# but, it's not the same with the string (string interning) and small intigers
# (ex.-5 -> 256, it depends what env and ver py we are working with)- unexpected result, more memory efficient

e = 'Hello, World!'
f = 'Hello, World!'

print(e is f)  # True
print(f is e)  # True
