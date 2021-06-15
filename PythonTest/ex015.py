n = s = 0
while True:
    n = int(input('Enter here a number(999 to finish program): '))
    if n == 999:
        break
    s += n
"""print('The sum of them is {}.'.format(s))"""
print(f'The sum of them is {s}.')
