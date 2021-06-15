print('The sum of all the multiple odd numbers of 3 between 1 and 500.')
play = input('Press "ENTER" to start')
s = 0
n = 0
#for c in range(1, 501):
#    if c % 3 == 0 and c % 2 != 0:
#        s = s + c
for c in range(1, 501, 2):
    if c % 3 == 0:
        n += 1
        s += c
print('The sum of the {} terms is {}'.format(n, s))
