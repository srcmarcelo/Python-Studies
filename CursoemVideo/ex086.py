l1 = []
for m in range(0, 3):
    for d in range(0, 3):
        n = int(input(f'Enter here a number to the position[{m}, {d}]: '))
        l1.append(n)
print('-='*25)
for d in range(0, 9):
    print(f'[{l1[d]:^3}]', end='' if d != 2 and d != 5 and d != 8 else '\n')
