from time import sleep
print('='*10, '{}'.format(' COUNTDOWN TO THE NEW YEAR '), '='*10)
play = input('Press "ENTER" to star: ')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('HAPPY NEW YEAR!!!!!!!')
