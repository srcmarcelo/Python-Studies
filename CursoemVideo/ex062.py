print('\33[31m='*10, ' Arithmetic Progression Maker (3.0) ', '='*10)
A1 = float(input('\33[mEnter here the First Term of the arithmetic progression: '))
r = float(input('Enter here the rate of the arithmetic progression: '))
n = 1
An = A1
t = 0
m = 10
while m != 0:
    t += m
    while n != t + 1:
        An = An + r
        print('A{:.0f} = {:.0f}'.format(n, An - r))
        n += 1
    m = int(input('How many more terms do you wanna see?(Enter "0" to finish program): '))
