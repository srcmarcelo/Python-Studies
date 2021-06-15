from datetime import date
s = 0
for c in range(0, 7):
    n = int(input('Enter here a person`s year of birth: '))
    if date.today().year - n >= 18:
        s = s + 1
    else:
        s = s + 0
print('{} of those are of legal age.'.format(s))
