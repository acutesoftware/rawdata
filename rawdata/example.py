# example.py

import generate as generate # prefix with rawdata. after pip install
import create as create     # prefix with rawdata. after pip install

print('Random Number    = ', generate.random_int(1,100))
print('Random Letters   = ', generate.random_letters(40))
print('Random Password  = ', generate.generate_password())

colLabel = ['DATE', 'name', 'password', 'Born',  'Quote', 'Score']
colTypes = ['DATE', 'PEOPLE', 'STRING', 'PLACE', 'WORD',  'INT']

words = generate.get_list_words()
print(len(words), ' words : ', words[500:502])

places = generate.get_list_places()
print(len(places), ' places : ', places[58:60])

tbl = generate.random_table(6,4, colTypes, colLabel)
generate.show_table(tbl)
print('Random Table     = ', len(colLabel), 'cols by ', len(tbl), ' rows')
print('tbl[0][0] = ', tbl[0][0] )

print('tbl[0][1] = ', tbl[0][1] )

print('tbl[1][0] = ', tbl[1][0] )

# now add some DQ issues
import create
t = create.Table(tbl, generate.random_letters(6))
t.swap_columns(0,3)
print(t.tbl)
t.add_errors(2)
print(t.tbl)
