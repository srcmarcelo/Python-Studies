city = input('What city do you live? ')
cut = city.upper().split()
print('"Santo" is the first name of your city. {}'.format('SANTO' in cut[0]))
