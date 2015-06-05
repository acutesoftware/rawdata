=========================================
Raw Data
=========================================

Generate realistic raw datasets with optional DQ issues

To install run 

.. code:: python

    pip install rawdata



Basic Usage
----------------


.. code:: python

    import rawdata.generate as generate

    print('Random Number    = ', generate.random_int(1,100))
        > Random Number    =  84

    print('Random Letters   = ', generate.random_letters(40))
        > Random Letters   =  T1CElkRAGPAmWSavbDItDbFmQIvUh26SyJE58x49

    print('Random Password  = ', generate.generate_password())
        > Random Password  =  peujlsmbf19966YKCX

    words = generate.get_list_words()
    print(len(words), ' words : ', words[500:502])
        > 10739  words :  ['architeuthis', 'arcsine']

    places = generate.get_list_places()
    print(len(places), ' places : ', places[58:60])
        > 262  places :  ['Brazil', 'British Virgin Islands']

    tbl = generate.random_table(6,4, colTypes, colLabel)
    generate.show_table(tbl)

        > DATE,name,Born
        > 2013,Douglas,Scandinavia
        > 1999,Hunter,Sierra Leone
        > 2005,Shubha,Madagascar
        
Adding Errors to a table


.. code:: python

    import create
    t = create.Table(tbl, generate.random_letters(6))
    t.add_errors(2)
    print(t.tbl)

And after adding 2 random errors there are additional spaces in Douglas, and the Born column is missing for Hunter


.. code:: python

    DATE    name       Born
    -----   ---------  ----------
    2013     Douglas   Scandinavia
    1999    Hunter      
    2005    Shubha     Madagascar




More information is at https://github.com/acutesoftware/rawdata


