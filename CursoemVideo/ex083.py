e = str(input('Enter here an expression: '))
e.split()
a = b = 0
for c in e:
    if c == '(':
        a += 1
    if c == ')':
        b += 1
if a == b:
    print('The expression is valid!')
else:
    print('The expression is invalid!')
