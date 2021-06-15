"""c = str(input('Enter here your gender (M/F): ')).upper()
while c != 'M' and c != 'F':
    print('ERROR')
    print('Enter the letter "M" for Male and "F" for Female.')
    c = str(input('Enter here your gender (M/F): ')).upper()
print('Thank you!')"""
c = str(input('Enter here your gender (M/F): ')).upper()
while c not in 'MF':
    print('ERROR')
    print('Enter the letter "M" for Male and "F" for Female.')
    c = str(input('Enter here your gender (M/F): ')).upper()
print('Thank you!')
