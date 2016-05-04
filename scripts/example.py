#!/usr/bin/python3
# example.py

import os
import sys

root_fldr = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'rawdata'))
test_fldr = os.path.dirname(__file__) + os.sep + 'test_results'
sys.path.insert(1, root_fldr)

test_fldr = os.path.dirname(__file__) + os.sep + 'test_results'
root_path = root_fldr + os.sep + 'samples'


import generate
import errors
import content

n = generate.NumberGenerator()
s = generate.StringGenerator()

print('Random Number    = ', n.random_int(1,100))
print('Random Currency  = ', n.random_currency(40))
print('Random Letters   = ', s.random_letters(40))
print('Random Password  = ', s.generate_password())


words = generate.get_list_words()
print(len(words), ' words : ', words[500:502])

places = generate.get_list_places()
print(len(places), ' places : ', places[58:60])

colLabel = ['DATE', 'name',   'Born']
colTypes = ['DATE', 'PEOPLE', 'PLACE']
tbl = generate.TableGenerator(3, colTypes, colLabel)
print(' ------- Random Table     = ', len(colLabel), 'cols by ', len(tbl.tbl), ' rows ------- ')
print(tbl)
#print('tbl[0][0] = ', tbl.tbl[0][0] )  # tbl[0][0] =  DATE
#print('tbl[0][1] = ', tbl.tbl[0][1] )  # tbl[0][1] =  name
#print('tbl[1][0] = ', tbl.tbl[1][0] )  # tbl[1][0] =  2013

# now add some DQ issues
t = errors.TableWithErrors(tbl, s.random_letters(6))
t.add_errors(2)
print(t.tbl)
#tbl.save_table('data' + os.sep + 'tbl_errors.csv')


custom_list = ['Carved Statue', '1984 Volvo', '2 metre Ball of string']
tbl = generate.TableGenerator(5, ['PEOPLE', 'INT', custom_list], ['Name', 'Age', 'Fav Possession'])
print(tbl)


# Create a large table
lbl = ['Year', 'Customer_id', 'Age', 'Name', 'Country', 'Details', 'Amount']
tpe = ['DATE', 'STRING', 'INT', 'PEOPLE', 'PLACE', 'WORD', 'CURRENCY']
t2 = generate.TableGenerator(500, tpe, lbl)
print('created table containing ' + str(len(t2.tbl)) + ' rows')
t2.save_table(generate.dat_fldr + os.sep + 'sample.csv')
for r in t2.tbl[0:4]:
    print(r)

    # created table containing 50001 rows
    # ['Entry Year', 'Name', 'Country', 'Travel Cost']
    # [1985, 'Rena', 'Samoa', '$90.95']
    # [1998, 'Gary', 'Sri Lanka', '$9.10']
    # [2002, 'Maire', 'Nauru', '295.10']
  
print('Example using sample config files')
s = content.Samples(root_path)
f = s.get_sample_by_name('finance_transaction')
print(f)

t3 = generate.TableGenerator(6, tpe, lbl)
print(t3)
   
# created table containing 7 rows
# ['Date', 'Details', 'Location', 'Amount']
# [2014, 'jack benny', 'Bermuda', '+$459.99']
# [1995, 'audubon', 'Runion', '$ 350.95']
# [1994, 'horace mann', 'Hong Kong', '463.95']
# [1988, 'culex pipiens', 'The West', '-$462.00']
# [2010, 'family convolvulaceae', 'Central Asia', '-136.00']
# [2009, 'grappling', 'Pitcairn', '-$83.00']    

# print('DATA FILES')
# d = content.DataFiles()
# print(d)
# T:\user\dev\src\python\rawdata\rawdata\data\countries.csv
# T:\user\dev\src\python\rawdata\rawdata\data\sample.csv
# T:\user\dev\src\python\rawdata\rawdata\data\names.csv


print('All Columns')
d = content.DataFiles()
for row in d.lookup:
    print(row)

