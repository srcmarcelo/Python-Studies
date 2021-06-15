import random
print('Let`s decide the sequence of the presentation. Put here the name of 4 students randomly')
A = input('First one: ')
B = input('Second one: ')
C = input('other one: ')
D = input('The last one: ')
List = [A, B, C, D]
random.shuffle(List)
print('The sequence is: {}'.format(List))
