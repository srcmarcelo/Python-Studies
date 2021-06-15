print('Enter here two numbers:')
n1 = float(input('N1: '))
n2 = float(input('N2: '))
print('-'*8, ' MENU ', '-'*8)
print('Choose what you wanna do with them.')
print('[1] = ADD\n[2] = MULTIPLY\n[3] = THE BIGGEST ONE\n[4] = NEW NUMBERS\n[5] = EXIT PROGRAM')
c = int(input('Your Choice: '))
while c != 5:
    if c == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    if c == 2:
        print('{} * {} = {}'.format(n1, n2, n1 * n2))
    if c == 3:
        if n1 > n2:
            print('The number {} is the biggest one.'.format(n1))
        if n1 < n2:
            print('The number {} is the biggest one.'.format(n2))
    if c == 4:
        n1 = float(input('N1: '))
        n2 = float(input('N2: '))
    print('[1] = SUM\n[2] = MULTIPLY\n[3] = THE BIGGEST ONE\n[4] = NEW NUMBERS\n[5] = EXIT PROGRAM')
    c = int(input('Your Choice: '))
