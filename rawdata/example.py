# example.py

import generate as generate # prefix with rawdata. after pip install
import create as create     # prefix with rawdata. after pip install

print('Random Number    = ', generate.random_int(1,100))
print('Random Number    = ', generate.random_letters(40))
print('Random Password  = ', generate.generate_password())

colLabel = ['DATE', 'name', 'password', 'Born',  'Quote', 'Score']
colTypes = ['DATE', 'PEOPLE', 'STRING', 'PLACE', 'WORD',  'INT']
tbl = generate.random_table(6,5, colTypes, colLabel)
print('Random Password  = ', len(colLabel), 'cols by ', len(tbl), ' rows')
generate.show_table(tbl)

words = generate.get_list_words()
print(len(words), ' words : ', words[500:502])

places = generate.get_list_places()
print(len(places), ' places : ', places[58:60])

