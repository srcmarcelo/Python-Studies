def readInt(num):
    while True:
        m = (str(input(num)))
        if m.isnumeric():
            value = int(m)
            break
        else:
            print('\33[31mError: you have to enter an integer number.\33[m')
    return value


n = readInt('Enter here an integer number: ')
print('You entered the number {}.'.format(n))
