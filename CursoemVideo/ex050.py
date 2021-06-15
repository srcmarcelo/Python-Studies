s = 0
for c in range(0, 6):
    num = int(input('Enter here a integer number: '))
    if num % 2 == 0:
        s = num + s
print('The sum of the even numbers of those numbers is {}.'.format(s))
