print('Enter below 4 numbers between 1 and 10:')
c = 0
p = 0
n = (int(input('n1: ')), int(input('n2: ')), int(input('n3: ')), int(input('n4: ')))
for m in range(0, 4):
    # if n[m] == 9:
    # c += 1
    if n[m] % 2 == 0:
        p += 1
# print(f'The number 9 was entered {c} times.')
print(f'The number 9 was entered {n.count(9)} times.')
if 3 in n:
    print(f'The number 3 was first entered on the {n.index(3) + 1} position.')
print(f'There are {p} even numbers between those: ', end='')
for m in range(0, 4):
    if n[m] % 2 == 0:
        print(f'{n[m]} ', end='')
