num = int(input('Type here an integer number between 0 and 9999: '))
print('Typed number: {}'.format(num))
print('Its unit: {}'.format(num % 10))
print('Its ten: {}'.format(num // 10 % 10))
print('Its hundred: {}'.format(num // 100 % 10))
print('Its thousand: {}'.format(num // 1000 % 10))
