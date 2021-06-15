from random import randint
from time import sleep
from operator import itemgetter
j = {}
m = []
p = ''
for c in range(1, 5):
    d = randint(1, 6)
    print(f'Player{c}: {d}')
    sleep(1)
    j[f'Player{c}'] = d
m = sorted(j.items(), key=itemgetter(1), reverse=True)
print('-='*20)
for i, v in enumerate(m):
    print(f'Position number {i+1}: {v[0]} with {v[1]} points.')
