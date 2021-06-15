print('Enter below your weight in kg and your height in m to see your BMI.')
w = float(input('Your weight: '))
h = float(input('Your height: '))
IMC = w / h**2
if IMC < 18.5:
    print('Your BMI is {:.1f}, you are \33[30mUNDERWEIGHT\33[m.'.format(IMC))
elif 18.5 <= IMC < 25:
    print('Your BMI is {:.1f}, you are in a \33[34mNORMAL WEIGHT\33[m.'.format(IMC))
elif 25 <= IMC < 30:
    print('Your BMI is {:.1f}, you are \33[37mOVERWEIGHT\33[m.'.format(IMC))
elif 30 <= IMC < 40:
    print('Your BMI is {:.1f}, you are \33[31mOBESE\33[m.'.format(IMC))
elif IMC >= 40:
    print('Your BMI is {:.1f}, you are \33[35mMORBID OBESE\33[m.'.format(IMC))
