n1 = float(input('Type here your first score: '))
n2 = float(input('Now, the second one: '))
m = (n1 + n2)/2
print('The media of your scores is: \33[0;30m{:.1f}\33[m'.format(m))
if 6 <= m < 8:
    print('You did it! You can celebrate! But study harder next time to get a better score, it was shit.')
if 8 <= m < 9:
    print('It was a good score! Now you can just relax, \33[1;34myou passed\33[m.')
if 9 <= m < 10:
    print('It was a really good score! \33[1;33mCongratulations!\33[m')
if m == 10:
    print('Yes, the media is 10, "\33[1;33mPERFECT\33[m" is the is the word for you now.')
if 0 < m < 6:
    print('\33[1;31mYou did not pass\33[m, sorry. Study harder and don`t give up, you will get it!')
if 0 > m:
    print('You did not put it right, review that and try again.')
if 10 < m:
    print('You did not put it right, review that and try again.')
