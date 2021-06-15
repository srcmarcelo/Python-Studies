from time import sleep
from random import randint


def higher(num):
    print('Analyzing...')
    for m in num:
        print(m, end=' ')
        sleep(0.3)
    print()
    print(f'{len(num)} values were analyzed.')
    print(f'The highest number was {max(num)}')


v = randint(1, 10)
print(f'Times: {v}')
print('-='*30)
for c in range(0, v):
    sleep(2)
    lst = []
    v2 = randint(0, 10)
    if v2 == 0:
        print('Analyzing...')
        print('0 values were analyzed.\nThe highest number was 0')
    else:
        for a in range(0, v2):
            lst += [randint(0, 10)]
        higher(lst)
    print('-='*30)
print('End...')
