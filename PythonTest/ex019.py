test = ['Jacob', 22]
people = [test[:]]
test[0] = 'Mary'
test[1] = 34
people.append(test)
print(people)
people1 = [['Marcelo', 17], ['Ana', 18], people[0], people[1]]
print(people1)
print(people1[0][0])
print(people1[2][1])
for p in people1:
    print(p[0], end=' ')
for p in people1:
    print(p[1], end=' ')
