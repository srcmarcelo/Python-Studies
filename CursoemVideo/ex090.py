s = {'Name': input('Enter here the student`s name: '), 'Media': float(input('Enter here the media: ')), 'Situation': ''}
if s['Media'] >= 7:
    s['Situation'] = 'APPROVED'
else:
    s['Situation'] = 'DISAPPROVED'
for k, v in s.items():
    print(f'{k}: {v}')
