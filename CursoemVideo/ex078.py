L = []
for c in range(0, 5):
    L.append(int(input('Enter here a number: ')))
print(f'The BIGGEST value is {max(L)} in the position number ', end='')
for c, v in enumerate(L):
    if v == max(L):
        print(c + 1, end=' ')
print(f'\nThe SMALLEST value is {min(L)} in the position number ', end='')
for c, v in enumerate(L):
    if v == min(L):
        print(c + 1, end=' ')
