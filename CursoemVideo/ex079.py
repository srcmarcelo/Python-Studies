L = []
while True:
    a = ''
    n = int(input('Enter here a number: '))
    if n in L:
        print('ERROR: This number is already in the list.')
    else:
        L.append(n)
        print('The number has been added to the list.')
    while a != 'Y' and a != 'N':
        a = input('Do you want to continue[Y OR N]? ').upper()
    if a == 'N':
        break
L.sort()
print(f'you entered the number {L}')
