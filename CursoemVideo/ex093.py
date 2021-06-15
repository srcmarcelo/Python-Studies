d = {'Name': input('Player`s name: ')}
l1 = []
t = 0
j = int(input('How many games did he play? '))
for c in range(1, j+1):
    l1.append(int(input(f'How many goals did he get in the match number {c}? ')))
    t += l1[c-1]
d['Goals'] = l1[:]
d['Total'] = t
print('-='*15)
for k, v in d.items():
    print(f'{k}: {v}')
print('-='*15)
print(f'The player {d["Name"]} played {j} matches.')
for c in range(1, j+1):
    print(f'In the match {c}, he got {l1[c-1]} goals.')
print(f'Total of goals: {t}')
