L1 = []
L2 = []
L3 = []
while True:
    a = ''
    L1.append(int(input('Enter here a number: ')))
    while a != 'Y' and a != 'N':
        a = input('Do you want to continue[Y OR N]? ').upper()
    if a == 'N':
        break
for c in L1:
    if c % 2 == 0:
        L2.append(c)
    if c % 2 != 0:
        L3.append(c)
print('The lists have been created.')
print(f'L1: {L1}\nL2(Even numbers): {L2}\nL3(Odd numbers): {L3}')
