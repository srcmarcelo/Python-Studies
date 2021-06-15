l1 = [[], []]
for c in range(0, 7):
    n = int(input('Enter here a number: '))
    if n % 2 == 0:
        l1[0].append(n)
    else:
        l1[1].append(n)
l1[0].sort()
l1[1].sort()
print(f'Even numbers: {l1[0]}.\nOdd numbers: {l1[1]}')
