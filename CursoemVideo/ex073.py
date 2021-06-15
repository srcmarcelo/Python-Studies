t = ('Flamengo', 'Santos', 'Palmeiras', 'Gremio', 'Atletico-PR', 'Sao Paulo', 'Internacional', 'Corinthias',
     'Fortaleza', 'Goias', 'Bahia', 'Vasco', 'Atletico-MG', 'Fluminense', 'Botafogo',
     'Ceara', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avai')
print(f'The top 5 of the championship was: {t[:5]}.')
print(f'The 4 last ones was: {t[16:20]}.')
print(f'Alphabetic order: {sorted(t)}')
print(f'The soccer team Chapecoense was on the {t.index("Chapecoense") + 1} position.')
