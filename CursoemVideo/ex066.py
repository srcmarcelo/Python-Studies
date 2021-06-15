c = s = 0
while True:
    num = int(input('Enter here an integer number (Enter 999 to finish program): '))
    if num == 999:
        break
    c += 1
    s += num
print(f'You entered {c} numbers and the sum of them is {s}')
