print('Enter below the length of three lines in cm:')
l1 = float(input('L1: '))
l2 = float(input('L2: '))
l3 = float(input('L3: '))
if + (l2 - l3) < l1 < l2 + l3 and + (l1 - l3) < l2 < l1 + l3 and + (l2 - l1) < l3 < l2 + l1:
    print('The lines with lengths {}cm, {}cm and {}cm can form a triangle. '.format(l1, l2, l3), end='')
    if l1 == l2 == l3:
        print('It`s an \33[34mequilateral triangle\33[m.')
    elif l1 == l2 and l2 != l3 or l1 == l3 and l3 != l2 or l2 == l3 and l3 != l1:
        print('It`s an \33[34misosceles triangle\33[m.')
    else:
        print('It`s a \33[34mscalene triangle\33[m.')
else:
    print('Those lines cannot form a triangle.')
