from random import randint
from time import sleep


def raffle(lst):
    print('Drawing 5 numbers to the list: ', end='')
    for c in range(0, 5):
        n = randint(0, 10)
        lst += [n]
        sleep(0.5)
        print(n, end=' ')
    print('')


def se(lst):
    s = 0
    for m in lst:
        if m % 2 == 0:
            s += m
    print(f'Adding the even numbers of {lst} = {s}')


num = []
raffle(num)
se(num)
