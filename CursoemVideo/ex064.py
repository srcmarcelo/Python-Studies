n = int(input('Enter here a integer number(enter "999" to stop the program): '))
c = 1
s = n
while n != 999:
    n = int(input('Enter here a integer number(enter "999" to stop the program): '))
    s += n
    c += 1
print('You entered {} numbers and the sum of them is {}.'.format(c - 1, s - 999))
