import random
import playsound
print('Hi, do you wanna play a game?')
print('Let`s do in this way: I will choose a number between 0 and 5 and you will have to guess that.')
y = input('Enter here "YES" if you wanna play: ')
if y.upper() == 'YES':
    print('Ok, let`s go. I will choose that.')
    print('*thinking...*')
    ans = random.randint(0, 5)
    print('Ok, I already chose.')
    num = int(input('Enter here your guess between 0 and 5: '))
    print('And the number that I chose is...')
    playsound.playsound('ex028.mp3')
    print('Number: {}'.format(ans))
    if num == ans:
        playsound.playsound('ex028(1).mp3')
        print('Congratulations!')
    else:
        playsound.playsound('ex028(2).mp3')
        print('Hahaha, I won. You can try again if you want.')
else:
    print('Ok, go sucking a dick.')
