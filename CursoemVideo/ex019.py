import random
print('Ok, to choice the student who will have to clear the board, let`s make a raffle.')
A = str(input('Put here the name of one student: '))
B = str(input('One more: '))
C = str(input('One more: '))
D = str(input('The last one: '))
List = [A, B, C, D]
E = random.choice(List)
print('The chosen student was {}{}{}.'.format('\33[1;33m', E, '\33[m'))
