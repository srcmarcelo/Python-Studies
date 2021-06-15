C = str(input('What graduation do you want to do? ')).strip().capitalize()
# cut = C.lower().split() sempre coloque variaveis adicionais antes dos if`s
if C == 'Mathematics':
    print('I hope you become a really good mathematician, that`s the best school subject. I love you, Pythagoras.')
elif 'engineering' in C.lower() and C != 'Computer engineering':
    print('I hope you became a really good engineer, study hard!')
elif C.capitalize() == 'Computer engineering':
    print('That`s the best one! Let`s make a revolution on the technology!')
elif C.capitalize() == 'Computer science':
    print('That`s a really good one!')
else:
    print('I would not do that graduation.')
print('Good luck on your {} graduation.'.format(C.title()))
