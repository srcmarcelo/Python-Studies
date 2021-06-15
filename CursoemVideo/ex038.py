num1 = int(input('Enter here a integer number: '))
num2 = int(input('Another one: '))
if num1 > num2:
    print('The number \33[34m{}\33[m is the \33[34mbiggest\33[m one.'.format(num1))
elif num1 < num2:
    print('The number \33[34m{}\33[m is the \33[34mbiggest\33[m one.'.format(num2))
else:
    print('\33[33mThere is not\33[m a bigger value, both numbers are \33[34mequal\33[m.')
