L = []
for c in range(0, 5):
    p = float(input('Enter here a person`s weight: '))
    L += [p]
print('The biggest weight of those is {}Kg and the smaller one is {}Kg.'.format(max(L), min(L)))
