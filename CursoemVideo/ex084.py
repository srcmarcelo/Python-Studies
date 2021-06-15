l1 = []
l2 = []
p = b = s = 0
while True:
    r = ''
    n = (str(input('Enter here the name of a person: ')))
    p += 1
    a = (float(input('Enter here its weight: ')))
    if p == 1:
        b = s = a
        l1.append(n)
        l2.append(n)
    else:
        if a == b:
            l1.append(n)
        if a > b:
            b = a
            l1.clear()
            l1.append(n)
        if a == s:
            l2.append(n)
        if a < s:
            s = a
            l2.clear()
            l2.append(n)
    while r != 'Y' and r != 'N':
        r = input('Do you want to continue[Y OR N]? ').upper()
    if r == 'N':
        break
print('-='*30)
print(f'You entered {p} people to the list.')
print(f'Greatest weight: {b:.2f}kg\nHeavier people: {l1}\nLeast weight: {s:.2f}kg\nLighter people: {l2}')
