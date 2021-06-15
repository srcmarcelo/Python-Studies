from random import randint
from time import sleep
print(f'{" Mega Sena Simulator ":$^50}')
a = int(input('How many games do you want me to draw? '))
print('-='*4, f'Drawing {a} Games', '-='*4)
for c in range(1, a + 1):
    l1 = []
    for m in range(0, 6):
        while True:
            n = randint(1, 60)
            if n not in l1:
                break
        l1.append(n)
    l1.sort()
    print(f'Game {c}: {l1}')
    sleep(1)
print('-='*5, f'Good Luck!', '-='*5)
