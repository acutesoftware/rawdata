# example.py
import rawdata.generate
import rawdata.errors

n = rawdata.generate.NumberGenerator()
s = rawdata.generate.StringGenerator()

print('Random Number    = ', n.random_int(1,100))
print('Random Currency  = ', n.random_currency(40))
print('Random Letters   = ', s.random_letters(40))
print('Random Password  = ', s.generate_password())


words = rawdata.generate.get_list_words()
print(len(words), ' words : ', words[500:502])

places = rawdata.generate.get_list_places()
print(len(places), ' places : ', places[58:60])

colLabel = ['DATE', 'name',   'Born']
colTypes = ['DATE', 'PEOPLE', 'PLACE']
tbl = rawdata.generate.TableGenerator(3, colTypes, colLabel)
print(tbl)
print('Random Table     = ', len(colLabel), 'cols by ', len(tbl.tbl), ' rows')
print('tbl[0][0] = ', tbl.tbl[0][0] )
print('tbl[0][1] = ', tbl.tbl[0][1] )
print('tbl[1][0] = ', tbl.tbl[1][0] )

# now add some DQ issues
t = rawdata.errors.TableWithErrors(tbl, s.random_letters(6))
t.add_errors(2)
print(t.tbl)
#tbl.save_table('data' + os.sep + 'tbl_errors.csv')

# Create a large table
lbl = ['Entry Year', 'Name',   'Country', 'Travel Cost']
tpe = ['DATE', 'PEOPLE', 'PLACE', 'CURRENCY']
t2 = rawdata.generate.TableGenerator(50000, tpe, lbl)
print('created table containing ' + str(len(t2.tbl)) + ' rows')
for r in t2.tbl[0:4]:
    print(r)
"""
    created table containing 50001 rows
    ['Entry Year', 'Name', 'Country', 'Travel Cost']
    [1985, 'Rena', 'Samoa', '$90.95']
    [1998, 'Gary', 'Sri Lanka', '$9.10']
    [2002, 'Maire', 'Nauru', '295.10']
"""    

custom_list = ['Carved Statue', '1984 Volvo', '2 metre Ball of string']
tbl = rawdata.generate.TableGenerator(5, ['PEOPLE', 'INT', custom_list], ['Name', 'Age', 'Fav Possession'])
print(tbl)

