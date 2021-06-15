l2 = []
while True:
    d = {'Name': input('Player`s name: ')}
    j = int(input('How many games did he play? '))
    a = ''
    l1 = []
    t = 0
    for c in range(1, j+1):
        l1.append(int(input(f'How many goals did he get in the match number {c}? ')))
        t += l1[c-1]
    d['Goals'] = l1[:]
    d['Total'] = t
    l2.append(d.copy())
    while a != 'Y' and a != 'N':
        a = input('Do you want to continue[Y or N]? ').upper()
    if a == 'N':
        break
print('-='*30)
print('COD ', end='')
for c in d.keys():
    print(f'{c:<15}', end='')
print()
for k, v in enumerate(l2):
    print(f'{k + 1:<4}', end='')
    for c in v.values():
        print(f'{str(c):<15}', end='')
    print()
print('-='*30)
while True:
    a = int(input('Do you wanna see the analytics of which player(Enter "999" to stop program)? '))-1
    while 0 > a > len(l2) and a != 998:
        print(f'ERROR: there is not player number {a+1}')
        a = int(input('Do you wanna see the analytics of which player(Enter "999" to stop program? '))-1
    if a == 998:
        print('Exiting...')
        break
    else:
        print(f'-----Analytics of the player {l2[a]["Name"]}')
        for c in range(1, len(l2[a]["Goals"])+1):
            print(f'{" "*4}In the match {c}, he got {l2[a]["Goals"][c-1]} goals.')
