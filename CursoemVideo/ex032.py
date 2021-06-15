from datetime import date
Y = int(input('Enter here a random year to see if it`s a leap year, if you wanna see this years, enter "0": '))
if Y == 0:
    Y = date.today().year
if Y % 400 == 0 or Y % 100 != 0 and Y % 4 == 0:
    print('The year {} is a leap year.'.format(Y))
else:
    print('The year {} is a normal year, it is not a leap year.'.format(Y))
