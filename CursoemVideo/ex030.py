num = int(input('Enter here a integer number: '))
if num == 0:
    print('The number 0 is a neutral number.')
    exit()
if num % 2 == 0:
    print('The number {} is an even number.'.format(num))
else:
    print('The number {} is an odd number.'.format(num))
