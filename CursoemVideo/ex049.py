num = int(input('Enter here an integer number: '))
print('Here is the multiplication table of that number:')
#for c in range(1, 11):
#    if c != 10:
#        print('{} *  {} = {}'.format(num, c, num * c))
#    if c == 10:
#        print('{} * 10 = {}'.format(num, num * c))
for c in range(1, 11):
    print('{} * {:2} = {}'.format(num, c, num * c))
