S = int(input('How many Km/h are you driving your car? '))
D = S - 80
F = D * 7
if S > 80:
    print('The maximum speed is 80 Km/h, and you are you are {}Km/h over that.\nSo, you will have to pay R${:.2f} of fine.'
          .format(D, F))
else:
    print('You are ok.')
