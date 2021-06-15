print('\33[33m='*10, ' Arithmetic Progression Maker (2.0) ', '='*10)
A1 = float(input('\33[mEnter here the First Term of the arithmetic progression: '))
r = float(input('Enter here the rate of the arithmetic progression: '))
n = 1
while n != 11:
    An = A1 + (n - 1)*r
    print('A{:.0f} = {:.0f}'.format(n, An))
    n += 1
