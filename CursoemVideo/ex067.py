while True:
    num = int(input('Enter here an integer number to see its multiplication table: '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} * {c:2} = {num * c}')
print('Finish Program.')
