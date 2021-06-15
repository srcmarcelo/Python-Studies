phrase = str(input('Type here a random phrase: ')).strip()
print('The letter "A" appears {} times in that phrase.'.format(phrase.upper().count('A')))
print('It appears on the position number {} on that phrase at first.'.format(phrase.upper().find('A') + 1))
print('Besides that, the letter "A" appears on the position number {} at last.'.format(phrase.upper().rfind('A') + 1))
