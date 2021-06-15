print('Enter below the length of three lines in cm:')
l1 = float(input('L1: '))
l2 = float(input('L2: '))
l3 = float(input('L3: '))
if + (l2 - l3) < l1 < l2 + l3 and + (l1 - l3) < l2 < l1 + l3 and + (l2 - l1) < l3 < l2 + l1:
    print('The lines with lengths {}cm, {}cm and {}cm can form a triangle.'.format(l1, l2, l3))
else:
    print('Those lines cannot form a triangle.')
