from time import sleep


def cont(a, b, c):
    if c == 0:
        c = 1
    if a < b:
        for c in range(a, b+1, c):
            print(c, end=' ')
            sleep(0.3)
    else:
        if c > 0:
            c = -c
        else:
            c = c
        for c in range(a, b-1, c):
            print(c, end=' ')
            sleep(0.3)
    print()
    print('-=' * 20)


cont(1, 10, 1)
cont(10, 0, 2)
cont(int(input('Start: ')), int(input('End: ')), int(input('Rhythm: ')))
