"""
Practical Programming #1
Take 2 numeric input from user and interchange variable values
"""

a = int(input('Number #1: '))
b = int(input('Number #2: '))

c = a
a = b
b = c
print(f'Number #1: {a} and #2 {b}')

"""
Practical Programming #2
Print rectangle
*****
*   *
*   *
*****
"""
# Square:

amount = 5
base = amount * "*"

for i in range(1, amount):
    if i == 1 or i == amount - 1:
        print(base)
    else:
        print(base[0] + 3 * ' ' + base[-1])

# Rectangle:

first_value = int(input('First side of rectangle should be: '))
second_value = int(input('Second side of rectangle should be: '))

for i in range(1, first_value+1):
    for j in range(1, second_value+1):
        if i == 1 or i == first_value:
            print('*', end=' ')
        else:
            if j == 1 or j == second_value:
                print('*', end=' ')
            else:
                print(' ', end=' ')
    print()

"""
Practical Programming # 3
Print table where only print selective numbers:
11
22
33
44
55...
But those numbers are not multiple of 3,5 and 7.
"""

max_num = int(input('What is the largest number u are looking for?   '))
num = 11

while num <= max_num:
    if num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
        print(num)
    num += 11


"""
Practical Programming # 4
Write program to find factorial of a number (silnia!).
"""

number = int(input('Put a numer: '))
factorial_number = 1

while number != 0:
    factorial_number = number*factorial_number
    number -= 1
print(factorial_number)

"""
Practical Programming # 5
Write program to generate Fibonacci sequence.
Max number of sequence is input from the User.
"""

max_seq_num = int(input('To what numer should I count Fib seq? '))
prev_num = 0
number = 1
print(prev_num)
print(number)

while number <= max_seq_num:
    sums = number + prev_num
    print(sums)
    prev_num = number
    number = sums

"""
Practical Programming # 6
Write program to check if number is prime or not.
"""

check_number = int(input("What number do you want to check if it's prime(or not)?   "))

for num in range(2, check_number):
    if check_number % num == 0:
        print('Number is not Prime')
        break
else:
    print('Number is Prime')





