from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
for c in n:
    print(f'{c} ', end='')
print(f'\nThe biggest value is {max(n)} and the smallest value is {min(n)}.')
