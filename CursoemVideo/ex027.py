name = str(input('Type here your full name: ')).strip()
cut = name.split()
print('Name: {}.\nFirst name: {}.\nLast name: {}.'.format(name, cut[0], cut[len(cut) - 1]))
