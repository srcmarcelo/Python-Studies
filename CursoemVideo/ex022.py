name = input('What is your full name? ')
print('Your name with CapsLock: {}'.format(name.upper()))
print('Ignoring the capitalization: {}'.format(name.lower()))
print('There are {} letters in your name'.format(len(name.strip().replace(' ', ''))))
first = name.split()
print('And there are {} letters in you first name'.format(len(first[0])))
