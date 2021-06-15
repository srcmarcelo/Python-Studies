people = {'name': 'Marcelo', 'gender': 'M', 'age': 17}
print(people)
print(people['name'])
people['weight'] = 54
for k, v in people.items():
    print(f'{k}: {v}')
del people['weight']
