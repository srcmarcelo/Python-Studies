l1 = []
while True:
    a = ''
    n = input('Name: ')
    s1 = float(input('Score 1: '))
    s2 = float(input('Score 2: '))
    l1.append([n, [s1, s2]])
    while a != 'Y' and a != 'N':
        a = input('Do you want to continue[Y OR N]? ').upper()
    if a == 'N':
        break
print('-='*25)
print('No.  Name          Media')
print('-'*30)
for c in range(0, len(l1)):
    print(f'{c:<5}{l1[c][0]:<14}{(l1[c][1][0]+l1[c][1][1])/2:.1f}')
print('-'*30)
while True:
    s = int(input('Do you wanna see which student`s score (Enter 999 to stop program)? '))
    if s == 999:
        break
    else:
        print(f'{l1[s][0]} got the scores {l1[s][1]}')
    print('-'*30)
print('End...')
