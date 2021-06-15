import math
num = int(input('Just type a number: '))
root = math.sqrt(num)
power = math.pow(num, 3)
log = math.log2(num)
print('The square root of that is: {}\n'
      'The same number at the 3th power is: {}\n'
      'And its logarithm is {}'.format(math.ceil(root), power, math.ceil(log)))
