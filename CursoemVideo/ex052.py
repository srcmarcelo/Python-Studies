num = int(input('Enter here a integer number: '))
r = 0
for c in range(1, num + 1):
    if num % c == 0 and c != 1 and c != num:
        print('\33[31m', end='')
    else:
        print('\33[33m', end='')
    if num % c == 0:
        r += 1
    print('{} '.format(c), end='')
if r == 2:
    print('\n\033[mIt`s prime number.')
else:
    print('\n\033[mIt`s not a prime number.')
