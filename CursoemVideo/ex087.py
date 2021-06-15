l1 = []
sp = l2 = 0
for m in range(0, 3):
    for d in range(0, 3):
        n = int(input(f'Enter here a number to the position[{m}, {d}]: '))
        l1.append(n)
print('-='*25)
for d in range(0, 9):
    print(f'[{l1[d]:^3}]', end='' if d != 2 and d != 5 and d != 8 else '\n')
for c in l1:
    if c % 2 == 0:
        sp += c
l2 = l1[3]
for c in l1[4:6]:
    if c > l2:
        l2 = c
print('-='*25)
print(f'Sum of the even number: {sp}\nSum of the third column values: {l1[2]+l1[5]+l1[8]}'
      f'\nSecond line higher value: {l2}')
