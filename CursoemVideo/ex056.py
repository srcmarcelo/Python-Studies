LA = []
BAM = 0
OM = ''
NAF = 0
for c in range(1, 5):
    print('-'*5, ' {}ª Person '.format(c), '-'*5)
    n = str(input('Name: '))
    a = int(input('Age: '))
    s = str(input('Gender(M/F): '))
    LA += [a]
    if s.upper() == 'M' and c == 1:
       OM = n
       BAM = a
    elif s.upper() == 'M' and c != 1:
        if a > BAM:
            OM = n
            BAM = a
    elif s.upper() == 'F' and a > 20:
        NAF += 1
print('The media os the ages is: {} years.'.format((sum(LA) / len(LA))))
print('The older man is {} years old and his name is {}.'.format(BAM, OM))
print('{} women are under 20 years old.'.format(NAF))
