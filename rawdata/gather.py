#!/usr/bin/python3
# gather.py



lookup_terms = [
   {'program' :'email_outlook.py',
    'known_as':['email', 'mail', 'outlook', 'messages', 
                'sent items', 'inbox', 'spam']
   },
   {'program' :'sys_PC_usage.py',
    'known_as':['PC usage', 'Application logging']
   },
   {'program' :'sys_process_windows.py',
    'known_as':['process']
   },
   #{'program' :'collect_bookmarks.py',
   # 'known_as':['chrome', 'bookmarks', 'browsing history', 'messages', 
   #             'sent items', 'inbox', 'spam']
   #},
   ]
   


def TEST():
    """
    This is the main function gather which defines 
    what programs are setup to collect and the data
    around them - it doesnt store access details like
    passwords and where to save outputs but rather is 
    a simple structure to let the calling module (such 
    as AIKIF, vais) know what is available and how to
    run it
    """
    for l in lookup_terms:
        print(l['program'] + ' = ', ','.join([t for t in l['known_as']]))
    
    
    
TEST()