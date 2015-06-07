=========================================
Raw Data
=========================================

.. image:: https://badge.fury.io/py/rawdata.svg
    :target: http://badge.fury.io/py/rawdata 

.. image:: https://landscape.io/github/acutesoftware/rawdata/master/landscape.svg?style=flat
   :target: https://landscape.io/github/acutesoftware/rawdata/master
   :alt: Code Health    
    
Generate realistic raw datasets with optional DQ issues

To install run 

.. code:: python

    pip install rawdata



Basic Usage
----------------

Create a random table

.. code:: python

    import rawdata.generate
    colLabel = ['Year', 'Name',   'Born']
    colTypes = ['DATE', 'PEOPLE', 'PLACE']
    tbl = rawdata.generate.TableGenerator(3, colTypes, colLabel)
    print(tbl)

        > Year,name,Born
        > 2013,Douglas,Scandinavia
        > 1999,Hunter,Sierra Leone
        > 2005,Shubha,Madagascar
        
Adding Errors to a table


.. code:: python

    import rawdata.errors
    t = rawdata.create.Table(tbl, 'BAD_STRING')
    t.add_errors(2)
    print(t.tbl)

And after adding 2 random errors there are additional spaces in Douglas, and the Born column is missing for Hunter


.. code:: python

    Year    Name       Born
    -----   ---------  ----------
    2013     Douglas   Scandinavia
    1999    Hunter      
    2005    Shubha     Madagascar


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



More information is at https://github.com/acutesoftware/rawdata


