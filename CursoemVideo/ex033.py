print('Enter bellow three different integers.')
n1 = int(input('n1: '))
n2 = int(input('n2: '))
n3 = int(input('n3: '))
if n1 > n2 > n3:
    print('The number {} is the biggest one and the number {} is the smaller one.'.format(n1, n3))
if n1 < n2 < n3:
    print('The number {} is the biggest one and the number {} is the smaller one.'.format(n3, n1))
if n1 > n3 > n2:
    print('The number {} is the biggest one and the number {} is the smaller one.'.format(n1, n2))
if n3 > n1 > n2:
    print('The number {} is the biggest one and the number {} is the smaller one.'.format(n3, n2))
if n2 > n1 > n3:
    print('The number {} is the biggest one and the number {} is the smaller one.'.format(n2, n3))
if n2 > n3 > n1:
    print('The number {} is the biggest one and the number {} is the smaller one.'.format(n2, n1))
