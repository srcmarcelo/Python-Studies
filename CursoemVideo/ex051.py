print('\33[34m='*10, ' Arithmetic Progression Maker ', '='*10)
A1 = float(input('\33[mEnter here the First Term of the arithmetic progression: '))
r = float(input('Enter here the rate of the arithmetic progression: '))
for n in range(1, 11):
    An = A1 + (n - 1) * r
    print('A{:.0f} = {:.0f}'.format(n, An))
