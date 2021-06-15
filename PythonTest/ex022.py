def so(a, b):
    print(f'a = {a}\nb = {b}')
    s = a + b
    print(s)
    print('-' * 10)


so(b=5, a=2)
so(20, 5)
so(int(input('a = ')), 9)

print(f'{"Test2":-^30}')


def cont(*num):
    s = 0
    for c in num:
        s += c
    print(s)
    print('-' * 30)


cont(4, 2, 7, 10)
