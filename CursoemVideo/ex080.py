L = []
for c in range(0, 5):
    n = int(input('Enter here a number: '))
    '''if c == 0:
        L.append(n)
    if c == 1:
        if n > L[0]:
            L.append(n)
        else:
            L.insert(0, n)
    if c == 2:
        if n > L[1]:
            L.append(n)
        if L[0] < n < L[1]:
            L.insert(1, n)
        if n < L[0]:
            L.insert(0, n)
    if c == 3:
        if n > L[2]:
            L.append(n)
        if L[1] < n < L[2]:
            L.insert(2, n)
        if L[0] < n < L[1]:
            L.insert(1, n)
        if n < L[0]:
            L.insert(0, n)
    if c == 4:
        if n > L[3]:
            L.append(n)
        if L[2] < n < L[3]:
            L.insert(3, n)
        if L[1] < n < L[2]:
            L.insert(2, n)
        if L[0] < n < L[1]:
            L.insert(1, n)
        if n < L[0]:
            L.insert(0, n)'''
    if c == 0 or n > L[-1]:
        L.append(n)
    else:
        pos = 0
        while pos < len(L):
            if n <= L[pos]:
                L.insert(pos, n)
                break
            pos += 1
    print(f'The number was added in the position {L.index(n)} of the list.')
print(f'You entered the numbers {L}.')
