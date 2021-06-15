a = int(input('How old are you? '))
if a < 18 and 18 - a != 1:
    print('You will have to enlist in the army in {} years.'.format(18 - a))
elif 18 - a == 1:
    print('You will have to enlist in the army next year.')
elif a == 18:
    print('It`s time for you to enlist in the army.')
elif a > 18 and a - 18 != 1:
    print('You should have already enlisted in the army! You are {} years late, you better run!'.format(a - 18))
elif a - 18 == 1:
    print('You should have already enlisted in the army! You should have done it last year.')
