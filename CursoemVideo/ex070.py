s = c = 0
nps = ''
ps = 99999999999
while True:
    n = str(input('Enter here the name of the product: '))
    p = float(input('Enter here how much it costs in R$: '))
    s += p
    if p > 1000:
        c += 1
    if p < ps:
        ps = p
        nps = n
    o = ''
    while o != 'Y' and o != 'N':
        o = str(input('Do you want to continue (Y or N)? ')).upper()
    if o == 'N':
        break
print(f'Cost: R${s:.2f}\nProducts over R$1000.00: {c}\nName of the shipper product: {nps} (R${ps:.2f})')
