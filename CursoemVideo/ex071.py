print('='*10, ' ATM ', '='*10)
c = int(input('Cash Withdrawal: R$'))
n50 = n20 = n10 = n1 = t = 0
r = c
while True:
    if c // 50 != 0:
        n50 = c // 50
        t += n50 * 50
        if t == c:
            break
        r = c % 50
    if r // 20 != 0:
        n20 = r // 20
        t += n20 * 20
        if t == c:
            break
        r = r % 20
    if r // 10 != 0:
        n10 = r // 10
        t += n10 * 10
        if t == c:
            break
        r = r % 10
    if r // 1 != 0:
        n1 = r // 1
        t += n1 * 1
        if t == c:
            break
if n50 > 0:
    print(f'Notes of R$50: x{n50}')
if n20 > 0:
    print(f'Notes of R$20: x{n20}')
if n10 > 0:
    print(f'Notes of R$10: x{n10}')
if n1 > 0:
    print(f'Notes of R$1 : x{n1}')
print(f'Total: R${t:.2f}')
print('Have a nice day!')
