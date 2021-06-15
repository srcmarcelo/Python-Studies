def factorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Enter here a number: '))
print(f'The factorial of {n} is equal to {factorial(n)}')


def par(m=0):
    if m % 2 == 0:
        return True
    else:
        return False


s = int(input('Enter here a number: '))
if par(s):
    print('Even number.')
else:
    print('Odd number.')
