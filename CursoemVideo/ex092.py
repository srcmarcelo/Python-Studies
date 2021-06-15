from datetime import datetime
d = {'Name': input('Name: '), 'Age': datetime.today().year - int(input('Year of birth: ')),
     'CTPS': int(input('Work Card ("0" = do not have): '))}
if d['CTPS'] != 0:
    d['Contracting'] = int(input('Year of contracting: '))
    d['Salary'] = float(input('Work payment per month: '))
    d['Retirement'] = d['Contracting'] - (datetime.today().year - d['Age']) + 35
    print('-=' * 20)
else:
    print('-=' * 20)
for k, v in d.items():
    print(f'{k}: {v}')
