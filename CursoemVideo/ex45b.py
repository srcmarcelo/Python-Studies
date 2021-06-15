from random import randint
from time import sleep
print('Hello! Let`s play some \33[31mRock\33[m \33[1;30mPaper\33[m \33[34mScissors\33[m?')
a = str(input('Enter here "YES" if you want to play with me: '))
if a.upper() != "YES":
    print('Ok, have a nice day!')
else:
    print('Let`s do that in this way: I will choose first, but you won`t see that, and than, you will make your choose.')
    sleep(5)
    print('\33[31mROCK\33[m     = 0\n\33[1;30mPAPER\33[m    = 1\n\33[34mSCISSORS\33[m = 2')
    print('Now I will choose mine.')
    j = ['\33[31mROCK\33[m', '\33[1;30mPAPER\33[m', '\33[34mSCISSORS\33[m']
    print('Thinking...')
    sleep(4)
    PC = randint(0, 2)
    print('Ok, I already chose. Your time.')
    P = int(input('Your choice(0, 1 or 2): '))
    print('Let`s see who wins!')
    sleep(2)
    print('My choice:   {}'.format(j[PC]))
    print('Your choice: {}'.format(j[P]))
    print('{} VS {}'.format(j[PC], j[P]))
    if P == 0 and PC == 1:
        print('\33[1;31mYOU LOSE\33[m')
    elif P == 0 and PC == 2:
        print('\33[1;33mYOU WIN\33[m')
    elif P == 1 and PC == 0:
        print('\33[1;33mYOU WIN\33[m')
    elif P == 1 and PC == 2:
        print('\33[1;31mYOU LOSE\33[m')
    elif P == 2 and PC == 0:
        print('\33[1;31mYOU LOSE\33[m')
    elif P == 2 and PC == 1:
        print('\33[1;33mYOU WIN\33[m')
    elif P == PC:
        print('\33[1;30mTIE\33[m')
