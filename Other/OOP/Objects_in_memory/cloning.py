a = [1, 2, 3, 4, 5]
b = a[:]

b[0] = 15

print(a)
print(b)

# cloning is opposite to aliasing

# ______________________________________


def remove_even_values(dictionary):
    for key, value in dictionary.copy().items():
        if value % 2 == 0:
            del dictionary[key]


my_dictionary = {"a": 1, "b": 2, "c": 3, "d": 4}

remove_even_values(my_dictionary)
print(my_dictionary)


# ______ Assignment: original list should not be changed ______

a = [7, 3, 6, 8, 2, 3, 7, 2, 6, 3, 6]
b = a
c = b
b = c


def remove_elem(data, target):
    data_copy = data.copy()
    for item in data:
        if item == target:
            data_copy.remove(target)
    return data_copy


def get_product(data):
    total = 1
    for i in range(len(data)):
        total *= data[i]
    return total


remove_elem(c, 3)
print(get_product(b))
print(a)



