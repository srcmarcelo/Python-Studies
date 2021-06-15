D = int(input('how many day did you rent the car? '))
KM = float(input('and how many kilometers did you drive it? '))
print('so, you have to pay R${:.2f} for the rent of the car.'.format(D*60 + KM*0.15))
