L = []
while True:
    a = ''
    L.append(int(input('Enter here a number: ')))
    while a != 'Y' and a != 'N':
        a = input('Do you want to continue[Y OR N]? ').upper()
    if a == 'N':
        break
print('_'*50)
print(f'You entered {len(L)} numbers.')
L.sort(reverse=True)
print(f'Descending Order: {L}')
if 5 in L:
    print('The number 5 is in the list.')
else:
    print('There is no number 5 in the list.')
