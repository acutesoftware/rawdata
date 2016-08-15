=========================================
Raw Data
=========================================

.. image:: https://api.travis-ci.org/repositories/acutesoftware/rawdata.svg
    :target: https://travis-ci.org/acutesoftware/rawdata
    :alt: Build Status

.. image:: https://coveralls.io/repos/acutesoftware/rawdata/badge.svg?branch=master&service=github
  :target: https://coveralls.io/github/acutesoftware/rawdata?branch=master
  :alt: Coverage
   
.. image:: https://badge.fury.io/py/rawdata.svg
    :target: http://badge.fury.io/py/rawdata 
    
.. image:: https://landscape.io/github/acutesoftware/rawdata/master/landscape.svg?style=flat
   :target: https://landscape.io/github/acutesoftware/rawdata/master
   :alt: Code Health    

.. image:: https://requires.io/github/acutesoftware/rawdata/requirements.svg?branch=master
     :target: https://requires.io/github/acutesoftware/rawdata/requirements/?branch=master
     :alt: Requirements Status
     
Generate realistic raw datasets with optional DQ issues

To install run 

.. code:: python

    pip install rawdata



Basic Usage
----------------

Create a random table

.. code:: python

    import rawdata.generate
    colLabel = ['Year', 'Name',   'Born', 'Details' , 'Amount']
    colTypes = ['DATE', 'PEOPLE', 'PLACE', 'WORD',    'CURRENCY']
    tbl = rawdata.generate.TableGenerator(3, colTypes, colLabel)
    print(tbl)

    > Year, name,    Age, Born,         Details,      Amount       
    > 2013, Douglas, 34,  Scandinavia,  Bowling Ball, $34.95
    > 1999, Hunter,  65,  Sierra Leone, Fish,         12.00
    > 2005, Shubha,  18,  Madagascar,   screenplay,   -$231.00

        
Adding Errors to a table


.. code:: python

    import rawdata.errors
    t = rawdata.errors.TableWithErrors(tbl, 'BAD_STRING')
    t.add_errors(3)
    print(t.tbl)

And after adding 3 random errors there are additional spaces in Douglas, a fake string in Douglas Born column, and the Born column is missing for Hunter


.. code:: python

    Year    Name       Born
    -----   ---------  ----------
    2013     Douglas   BAD_STRING
    1999    Hunter      
    2005    Shubha     Madagascar

You can use columns generated via a custom list

.. code:: python


    custom_list = ['Carved Statue', '1984 Volvo', '2 metre Ball of string']
    tbl = TableGenerator(5, ['PEOPLE', 'INT', custom_list], ['Name', 'Age', 'Fav Possession'])
    print(tbl)
        > Name,   Age,  Fav Possession
        > Inez,    58,  Carved Statue
        > Zane,    50,  2 metre Ball of string
        > Jered,   49,  1984 Volvo
        > Tameron, 55,  2 metre Ball of string
        > Wyatt,   68,  Carved Statue

Other functions 

.. code:: python

    import rawdata.generate
    n = rawdata.generate.NumberGenerator
    s = rawdata.generate.StringGenerator

    print('Random Number    = ', n.random_int(1,100))
        > Random Number    =  84

    print('Random Letters   = ', s.random_letters(40))
        > Random Letters   =  T1CElkRAGPAmWSavbDItDbFmQIvUh26SyJE58x49

    print('Random Password  = ', s.generate_password())
        > Random Password  =  peujlsmbf19966YKCX

    words = rawdata.generate.get_list_words()
    print(len(words), ' words : ', words[500:502])
        > 10739  words :  ['architeuthis', 'arcsine']

    places = rawdata.generate.get_list_places()
    print(len(places), ' places : ', places[58:60])
        > 262  places :  ['Brazil', 'British Virgin Islands']


List of Column Types (Table Generator)
------------------------------------------


.. code:: python

    'INT'      - returns a number
    'CURRENCY' - returns a currency that may have strings $ / pounds
    'STRING'   - returns a random string
    'WORD'     - returns a word from nouns.csv
    'DATE'     - returns a date
    'YEAR'     - returns a year. Both year and date can have ranges set via set_range()
    'PLACE'    - returns a location from country.csv
    'PEOPLE'   - returns a name from names.csv
    [list]     - pass any list to return a random choice from it
                    (e.g. my_colours = ['Blue', 'Green', 'Orange'] )
                    
                    


More information is at https://github.com/acutesoftware/rawdata


