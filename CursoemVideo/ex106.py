def h(d):
    print('\33[1;31m~'*23, '\33[m')
    print("\33[1;31m  Python's Help System ", '\33[m')
    print('\33[1;31m~'*23, '\33[m')
    help(d)
    return d


while True:
    a = input('Function or library(Enter "END" to stop program): ')
    if a.upper() == 'END':
        print('Exiting...')
        break
    h(a)
