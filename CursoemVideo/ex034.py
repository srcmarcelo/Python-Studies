M = float(input('how much do you earn in your job in R$? '))
i1 = M * 1.1
i2 = M * 1.15
if M > 1250.00:
    print('You just got an increase of 10% in your salary as a gift from the company.')
    print('Your salary is now R${:.2f}'.format(i1))
if M <= 1250.00:
    print('You just got an increase of 15% in your salary as a gift from the company.')
    print('Your salary is now R${:.2f}'.format(i2))
