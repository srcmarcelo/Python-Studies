p = str(input('Enter here a random phrase or name and let`s see if it`s a palindrome: ').strip().replace(' ', ''))
n = ''
for c in range(len(p) - 1, -1, -1):
    n += p[c]
print('The inverse of that {} is {}'.format(p.upper(), n.upper()))
if p == n:
    print('It`s a palindrome!')
else:
    print('It`s not a palindrome.')
