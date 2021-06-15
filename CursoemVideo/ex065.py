num = float(input('Enter here a number: '))
a = int(input('Do you wanna keep going? Enter 1 to "YES" and 0 to "NO": '))
s = num
L = [num]
c = 1
while a != 0:
    num = float(input('Enter here a number: '))
    s += num
    L += [num]
    c += 1
    a = int(input('Do you wanna keep going? Enter 1 to "YES" and 0 to "NO": '))
print('The media of the entered values is {}.\n{} was the biggest one.\n'
      '{} was the smaller one.'.format(s/c, max(L), min(L)))
