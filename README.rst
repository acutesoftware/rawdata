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

        > DATE,name,password,Born,Quote,Score
        > 1989,Ugo,qzMkTrHwQeNas3enkCYO,Yemen,mallow,94
        > 2009,Taffy,TDFz9BgjqRJLyPGyLKkW,Kenya,masquerade party,72
        > 2003,Forster,ui7VbzGG8wdGk9gUqAyb,Asia,suborder percoidea,47
        > 1997,Aldona,RsKN8hyL8MyxZ0E5Mjqq,Mozambique,apresoline,41

        
Adding Errors to the data


.. code:: python

    import create
    t = create.Table(tbl, generate.random_letters(6))
    print(t.tbl)
    
DATE	name	password	            Born	    Quote	        Score
2011	Jerusha	O96CpTp5aFqWNIAO22qP	Cuba	    ileocecal valve	68
2003	Qabil	UeDJwgQa1WNnV39REH8a	Afghanistan	nominative case	96
2003	Zazu	rfQ8OXGz8j9p5YJOijs5	Ukraine	    reading lamp	39
1997	Koda	EhEZvNtJcTTVtBd0mECc	Gibraltar	sangay	        99
    
.. code:: python
    
    t.add_errors(2)
    print(t.tbl)
    
DATE	name	password	            Born	    Quote	        Score
2011	Jerusha	O96CpTp5aFqWNIAO22qP	``u6YWTW``	    ileocecal valve	68
2003	Qabil	`` UeDJwgQa1WNnV39REH8a  ``   	Afghanistan	nominative case	96
2003	Zazu	rfQ8OXGz8j9p5YJOijs5	Ukraine	    reading lamp	39
1997	Koda	EhEZvNtJcTTVtBd0mECc	Gibraltar	sangay	        99




More information is at https://github.com/acutesoftware/rawdata


