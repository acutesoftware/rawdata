# install.py

import os
import sys

data_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + '..' + os.sep +  'rawdata' + os.sep + 'data' ) 

ndx_file = data_fldr + os.sep + '_index.ndx'

def main():
    print('install.py')
    print('Script to setup local data')
    print('folders, connections to databases, etc.\n')

    print('[TODO] Setup Local folder structure...')

    rebuild_index()

    print('Done')



def rebuild_index():
    """
    scans rawdata\data\ folders to create lookups
    of all tables, column names
    """
    print('Building indexes...')
    print(data_fldr)
    ndx = []
    for root, _, files in os.walk(data_fldr):
        for f in files:
            if f[-3:].upper() in ['CSV','TXT']:
                ndx.extend(get_index_terms(root + os.sep + f, f))
    with open(ndx_file, 'w') as fio:
        for i in ndx:
            fio.write(i + '\n')
    
def get_index_terms(fname, shortname):
    """
    reads the file 'fname' and returns all index values
    for it in terms of fname.col_name, e.g.
    finance_transactions.transaction_type
    """
    data_files = []
    terms = []
    folder_names = fname.split(os.sep)
    start = False
    root_name = ''
    for num, fldr in enumerate(folder_names):
        if start == True:
            root_name += fldr + '.'
        if fldr == 'data':
            start = True
    #print('fname = ', fname, ' root_name = ', root_name)    
    root_name = root_name[:-5]
    #terms.append(root_name)
    data_files.append(root_name)
    
    #read the file and add column names to list of terms
    with open(fname, 'r') as f:
        hdr = f.readline()
        cols = hdr.split(',')
        for col in cols:
            terms.append(root_name + '.' + col.strip(' ').strip('"').strip('\n'))
    
    return terms
    
main()