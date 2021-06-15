from random import randint
print('Let`s play \33[34mEven\33[m or \33[31mOdd\33[m!')
print('I will choose a number first and let`s see who wins.')
c = 0
print('Choose between Even or Odd first.')
while True:
    COM = randint(0, 10)
    EO = int(input('Enter "1" to Even and "0" to Odd: '))
    P = int(input('I already chose! Enter here a number between 0 and 10 as your choice: '))
    print(f'My choice:   {COM}\nYour choice: {P}')
    j = COM + P
    print(f'{COM} + {P} = {j}')
    if j % 2 == 0:
        print('It is an \33[34mEven\33[m number!')
    if j % 2 != 0:
        print('It is an \33[31mOdd\33[m number!')
    if EO == 1 and j % 2 == 0 or EO == 0 and j % 2 != 0:
        print('\33[33mYou win!\33[m Let`s play again.')
        c += 1
    else:
        break
if c > 0:
    print(f'\33[31mYou lose!\33[m You got {c} wins.')
else:
    print('\33[31mYou lose!\33[m')
