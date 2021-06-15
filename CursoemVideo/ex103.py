def token(a='<unknown>', b=0):
    print(f'The player {a} got {b} goal(s) on the championship.')


n = str(input('Player`s name: '))
g = str(input('Amount of goals: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    token(b=g)
else:
    token(n, g)
