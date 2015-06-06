# example.py

import rawdata.generate as generate 
import rawdata.create as create     

print('Random Number    = ', generate.random_int(1,100))
print('Random Letters   = ', generate.random_letters(40))
print('Random Password  = ', generate.generate_password())

colLabel = ['DATE', 'name',   'Born']
colTypes = ['DATE', 'PEOPLE', 'PLACE']

words = generate.get_list_words()
print(len(words), ' words : ', words[500:502])

places = generate.get_list_places()
print(len(places), ' places : ', places[58:60])

tbl = generate.random_table(3, colTypes, colLabel)
generate.show_table(tbl)
print('Random Table     = ', len(colLabel), 'cols by ', len(tbl), ' rows')
print('tbl[0][0] = ', tbl[0][0] )

print('tbl[0][1] = ', tbl[0][1] )

print('tbl[1][0] = ', tbl[1][0] )

# now add some DQ issues
t = create.Table(tbl, generate.random_letters(6))
#t.swap_columns(0,3)
print(t.tbl)
generate.save_table(tbl, 'tbl_orig.csv')
t.add_errors(2)
print(t.tbl)
generate.save_table(tbl, 'tbl_errors.csv')

# Create a large table
lbl = ['Entry Year', 'Name',   'Country', 'Travel Cost']
tpe = ['DATE', 'PEOPLE', 'PLACE', 'CURRENCY']
t2 = generate.random_table(5000, tpe, lbl)
generate.show_table(t2)