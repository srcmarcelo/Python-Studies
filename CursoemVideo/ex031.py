D = float(input('How far is the trip in Km? '))
P1 = D * 0.5
P2 = D * 0.45
if D <= 200:
    print('So, the price of the ticket will be R${:.2f}.'.format(P1))
else:
    print('So, the price of the ticket will be R${:.2f}.'.format(P2))
