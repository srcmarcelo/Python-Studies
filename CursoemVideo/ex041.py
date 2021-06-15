from datetime import date
print('\33[33m-=-\33[m' * 15)
print('\33[32m      National Swimming Confederation\33[m')
print('\33[33m-=-\33[m' * 15)
print('It`s a program created by the Brazilian Government to check the athlete category by age.')
y = int(input('Enter here the athlete`s year of birth: '))
age = date.today().year - y
print('The athlete`s age is: \33[1;30m{} years old\33[m'.format(age))
if 0 <= age <= 9:
    print('The athlete category is: \33[30mPRE CHILD\33[m')
elif age <= 14:
    print('The athlete category is: \33[36mCHILD\33[m')
elif age <= 19:
    print('The athlete category is: \33[34mJUNIOR\33[m')
elif age <= 25:
    print('The athlete category is: \33[35mSENIOR\33[m')
elif age > 25:
    print('The athlete category is: \33[37mMASTER\33[m')
