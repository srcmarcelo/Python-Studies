print('A store is giving 5% of discount at all products and do you wanna know the final price of some?')
print('I can help you.')
p = float(input('Type here the price of some product in dollars: '))
print('You gonna pay just ${} for that. You are welcome!'.format(p-(p*(5/100))))
