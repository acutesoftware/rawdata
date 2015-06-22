# example.py
import rawdata.generate
import rawdata.errors
import samples as samples  # change to rawdata.samples once uploaded to pypi

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


custom_list = ['Carved Statue', '1984 Volvo', '2 metre Ball of string']
tbl = rawdata.generate.TableGenerator(5, ['PEOPLE', 'INT', custom_list], ['Name', 'Age', 'Fav Possession'])
print(tbl)


# Create a large table
lbl = ['Year', 'Customer_id', 'Age', 'Name', 'Country', 'Details', 'Amount']
tpe = ['DATE', 'STRING', 'INT', 'PEOPLE', 'PLACE', 'WORD', 'CURRENCY']
t2 = rawdata.generate.TableGenerator(500, tpe, lbl)
print('created table containing ' + str(len(t2.tbl)) + ' rows')
t2.save_table('sample.csv')
for r in t2.tbl[0:4]:
    print(r)

    # created table containing 50001 rows
    # ['Entry Year', 'Name', 'Country', 'Travel Cost']
    # [1985, 'Rena', 'Samoa', '$90.95']
    # [1998, 'Gary', 'Sri Lanka', '$9.10']
    # [2002, 'Maire', 'Nauru', '295.10']
  
print('Example using sample config files')
s = samples.Samples()
f = s.get_sample_by_name('finance_transaction')
t3 = rawdata.generate.TableGenerator(6, f.col_types, f.col_labels)
print(t3)
   
# created table containing 7 rows
# ['Date', 'Details', 'Location', 'Amount']
# [2014, 'jack benny', 'Bermuda', '+$459.99']
# [1995, 'audubon', 'Runion', '$ 350.95']
# [1994, 'horace mann', 'Hong Kong', '463.95']
# [1988, 'culex pipiens', 'The West', '-$462.00']
# [2010, 'family convolvulaceae', 'Central Asia', '-136.00']
# [2009, 'grappling', 'Pitcairn', '-$83.00']    


