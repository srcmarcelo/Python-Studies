import random
import playsound
import time
print('-'*15, ' Let`s play a game ', '-'*15)
print('Let`s do in this way: I will choose a number between 0 and 10 and you will have to guess that.')
print('I will choose mine first.')
print('*Thinking...*')
ans = random.randint(0, 10)
time.sleep(2)
num = int(input('I am OK. Enter here a number between 0 and 10 as your guess: '))
print('Let`s see...')
time.sleep(2)
c = 1
while num != ans:
    playsound.playsound('ex028(2).mp3')
    print('I WIN!')
    if num > ans:
        print('Try another time! My choice is still the same and it`s \33[1;30mSMALLER\33[m than yours.')
    if num < ans:
        print('Try another time! My choice is still the same and it`s \33[1;30mBIGGER\33[m than yours.')
    c += 1
    num = int(input('Enter here another number between 0 and 10: '))
playsound.playsound('ex028(1).mp3')
print('You got that! The number that I chose is: {}.'.format(ans))
print('You had to try \33[31m{} TIMES\33[m to get that.'.format(c))
print('-'*10, ' YOU WIN! ', '-'*10)
