l = m = f2 = 0
while True:
    print('-'*40)
    print('Enter here the age and gender of a person.')
    print('-'*40)
    o = g = ''
    a = int(input('Age: '))
    while g != 'M' and g != 'F':
        g = str(input('Gender (M or F): ')).upper()
    print('-'*40)
    if a >= 18:
        l += 1
    if g == 'M':
        m += 1
    if g == 'F' and a < 20:
        f2 += 1
    while o != 'Y' and o != 'N':
        o = str(input('Do you want to continue (Y or N)? ')).upper()
    if o == 'N':
        break
print(f'{l} of those are over 18 years old.\n{m} of those are men.\n{f2} women of those are under 20 years old.')
