List = ('MOUSE', 'NOTEBOOK', 'COMPUTER', 'PENCIL', 'TABLE', 'PRINTER', 'CALCULUS', 'MATHEMATICS', 'MARCELO', 'RECIFE')
for c in List:
    print(f'\nIn the word {c} we have the vowels: ', end='')
    for m in c:
        if m in 'AEIOU':
            print(m, end=' ')
