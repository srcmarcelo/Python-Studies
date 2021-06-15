import time
print('Hey bro. I have a degree in accounting and I am here to tell you if '
      '{}you can{} finance the house or {}not{}.'.format('\33[34m', '\33[m', '\33[31m', '\33[m'))
P = float(input('What`s the \33[32mprice\33[m of the house in R$? '))
S = float(input('How much do you \33[32mearn\33[m per in month R$? '))
Y = int(input('For how many \33[32myears\33[m do you want to finance that? '))
B = P / (12*Y)
if B <= S * (3/10):
    print('Your house financing was...')
    time.sleep(3)
    print('\33[34mACCEPTED\33[M')
    print('The installments will cost {:.2f}'.format(B))
else:
    print('Your house financing was...')
    time.sleep(3)
    print('\33[31mREJECTED\33[m')
    print('To make that financing, the installments will cost R${:.2f}. It`s more than 30% of '
          'your salary.'.format(B))
