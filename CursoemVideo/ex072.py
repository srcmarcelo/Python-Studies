t = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
     'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')
while True:
    n = int(input('Enter here a integer number between 0 and 20 to see it written below: '))
    if 0 <= n < 21:
        break
print(f'n = {t[n]}')
