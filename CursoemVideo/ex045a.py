from random import randint
from time import sleep
print('Let`s play some even or odd? It will work in this way:\n'
      'You will choose between \33[34meven\33[m or \33[31modd\33[m.\n'
      'After that, I will choose a number and you will choose one too.\n'
      'If the sum of those numbers is the type of number you have chosen, you win. if it`s not, I win.')
t = str(input('Enter "even" if you wanna be even and "odd" if you wanna be odd: '))
if t.lower() == 'even' or t.lower() == 'odd':
    print('Now, I will choose a number.')
    print('Thinking...')
    c = randint(1, 10)
    sleep(3)
    print('Ok, your time.')
    num = int(input('Choose a integer number between 1 and 10: '))
    print('The number that I have chosen is {}'.format(c))
    print('The sum of them is {}'.format(c + num))
    if (c + num) % 2 == 0:
        print('It`s an \33[34mEVEN\33[m number.')
        if t.lower() == 'even':
            print('\33[1;33mYOU WIN\33[m')
        else:
            print('\33[1;30mYOU LOSE\33[m')
    else:
        print('It`s an \33[31mODD\33[m number.')
        if t.lower() == 'odd':
            print('\33[1;33mYOU WIN\33[m')
        else:
            print('\33[1;30mYOU LOSE\33[m')
else:
    print('ERROR')
    print('You can choose only "even" or "odd". Try again.')
