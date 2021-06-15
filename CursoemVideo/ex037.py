num = int(input('Type here a integer number: '))
print('Here below are the options to covert the number:')
print('1 = BINARY\n2 = OCTAL\n3 = HEXADECIMAL')
op = int(input('Your choice: '))
if op == 1:
    print('Number: {}\nConversion: {}'.format(num, bin(num)[2:]))
if op == 2:
    print('Number: {}\nConversion: {}'.format(num, oct(num)[2:]))
if op == 3:
    print('Number: {}\nConversion: {}'.format(num, hex(num)[2:]))
if op != 1 and op !=2 and op != 3:
    print('You can choose only the numbers 1, 2 or 3.')
