L1 = []
L2 = []
L3 = []
while True:
    a = ''
    L1.append(int(input('Enter here a number: ')))
    while a != 'Y' and a != 'N':
        a = input('Do you want to continue[Y OR N]? ').upper()
    if a == 'N':
        print('The list has been created.')
        break
print('Now lets create more 2 lists, one with \33[34mEVEN\33[m numbers and other with \33[31mODD\33[m numbers.')
while True:
    a = ''
    n = int(input('Enter here an even number: '))
    if n % 2 == 0:
        L2.append(n)
        print('The number has been added to the list.')
    else:
        print('ERROR: it is not an even number.')
    while a != 'Y' and a != 'N':
        a = input('Do you want to continue[Y OR N]? ').upper()
    if a == 'N':
        print('The list has been created.')
        break
while True:
    a = ''
    n = int(input('Enter here an odd number: '))
    if n % 2 != 0:
        L3.append(n)
        print('The number has been added to the list.')
    else:
        print('ERROR: it is not an odd number.')
    while a != 'Y' and a != 'N':
        a = input('Do you want to continue[Y OR N]? ').upper()
    if a == 'N':
        print('The list has been created.')
        break
print(f'L1: {L1}\nL2: {L2}\nL3: {L3}')
