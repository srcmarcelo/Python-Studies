"""num = int(input('Enter here a integer number to see its factorial: '))
r = 1
c = 0
while num != 1 and num != 0:
    r = num * r
    num -= 1
    c += 1
if num == 0:
    r = 1
print('The factorial of {} is {}.'.format(num + c, r))"""
"""from math import factorial
num = int(input('Enter here a integer number to see its factorial: '))
c = num
f = factorial(num)
print('{}! = {} '.format(num, num), end='')
while c > 1:
    c -= 1
    print('x {} '.format(c), end='')
print('= {}'.format(f))"""
from math import factorial
num = int(input('Enter here a integer number to see its factorial: '))
c = num
print('{}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print(factorial(num))
