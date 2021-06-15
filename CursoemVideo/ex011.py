print('Do you wanna know how many gallons of paint you have to buy to paint your room`s wall? I can help you.')
le = float(input('What`s the length of that wall in meters? '))
h = float(input('And the height? '))
A = le * h
print('1 litre can can painting 2m² of the wall and the wall is {:.0f}m²'.format(A))
print('So, you will need at least {}L of paint'.format(A / 2))
