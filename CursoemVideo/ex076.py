List = ('Notebook', 15, 'Computer', 1000, 'Printer', 300, 'Mouse', 20, 'Bird', 50, 'sua mae', 2)
print(f'{" List Of Prices ":-^44}')
for c in range(0, 11, 2):
    print(f'{List[c]:.<35}R${List[c+1]:7.2f}')
print('-'*44)
