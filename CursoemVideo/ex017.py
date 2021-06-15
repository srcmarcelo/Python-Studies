import math
print('Ok, you have a rectangle triangle and do you wanna know the measure of the hypotenuse?')
CO = float(input('How many centimeters is the opposite side of the triangle? '))
CA = float(input('And the adjacent side? '))
print('So, the measure os the hypotenuse is {:.2f}cm.'.format(math.hypot(CO, CA)))
