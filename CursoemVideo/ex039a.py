import datetime
y = int(input('Enter your year of birth here: '))
n = datetime.date.today().year
a = n - y
if a < 18:
    print('Your age right now: {}\nYou will have to enlist in the army in {} years.'.format(a, 18 - a))
    print('Year of enlist: {}'.format(n + (18 - a)))
if a == 18:
    print('It`s time for you to enlist in the army, you are 18 years old.')
if a > 18:
    print('Your age right now: {}\nYou should have already enlisted in the army, you are {} years late.'.format(a, a - 18))
    print('Year of enlist: {}'.format(n - (a - 18)))
