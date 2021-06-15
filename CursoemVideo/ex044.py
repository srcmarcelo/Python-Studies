print('\33[33m-=-\33[m' * 10)
print('\33[1;30m       Price Calculator')
print('\33[33m-=-\33[m' * 10)
p = float(input('Enter here the original price of the product in R$: '))
c = str(input('If you wanna pay that in sight, enter "YES", if not, enter "NO": '))
if c.upper() == "YES":
    f = int(input('How are you going to pay that? If it`s in cash or check, enter "1", if it`s on the card, enter "2": '))
    if f == 1:
        print('You will have a \33[34m10% discount\33[m on the product price, now it costs \33[1;30mR${:.2f}\33[m.'.format(p - (p*(10/100))))
    elif f == 2:
        print('You will have a \33[34m5% discount\33[m on the product price, now it costs \33[1;30mR${:.2f}\33[m.'.format(p - (p*(5/100))))
if c.upper() == "NO":
    i = int(input('Enter here how many installments you want (know it gonna be payed on the card): '))
    if i == 2:
        print('The price will stay the same.')
    elif i >= 3:
        print('The product price will have a \33[31m20% increase\33[m, now it costs \33[1;30mR${:.2f}\33[m.'.format(p * 1.2))
    elif i == 1:
        print('You will have a 5% discount on the product price, now it costs \33[1;30mR${:.2f}\33[m'.format(p - (p * (5 / 100))))
