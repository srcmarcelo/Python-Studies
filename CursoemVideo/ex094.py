l1 = []
s = 0
while True:
    d = {'Name': input('Name: '), 'Gender': input('Gender[M/F]: ').upper(), 'Age': int(input('Age: '))}
    s += d['Age']
    l1.append(d.copy())
    a = ''
    while a != 'Y' and a != 'N':
        a = input('Do you want to continue[Y OR N]? ').upper()
    if a == 'N':
        break
m = s / len(l1)
print('-='*20)
print(f'There are {len(l1)} people in the group.')
print(f'Media of age: {m:.2f}')
print('The women are: ', end='')
for c in l1:
    if c['Gender'] == 'F':
        print(c['Name'], end=' ')
print(f'\nPeople over media of age:')
for c in l1:
    if c['Age'] > m:
        for k, v in c.items():
            print(f'{k}: {v}', end='; ')
        print()
print('End...')
