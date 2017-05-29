#!/usr/bin/python3
# coding: utf-8
# identify_grain.py

import sys

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('.') if isfile(join('.', f))]

csv_files = []
for f in onlyfiles:
    if f[-3:] == 'csv' and f[0:6] == 'grain_':
        csv_files.append(f)


def main():
    for f in csv_files:
        res = identify_grain_csv(f)
        print('Grain of ' + f + ' is : ', res)
    
def load_to_array(name):
    arr = []
    with open (name, 'r') as f:
        for row in f:
            if row:
                arr.append([r.strip('\n').strip('"') for r in row.split(',')])
    return arr

def identify_grain_csv(fname):
    """
    get counts in all columns until matched count(*)
    to guess the grain of the current table
    """
    grain = ''
    tbl = load_to_array(fname)
    c = get_counts_by_col(tbl)
    for k,v in c.items():
        print(k,v)
        
    
    
    return grain
    
def get_counts_by_col(tbl):
    """
    get counts by all permutations of a table
    """
    cnt = {}
    for col_num, c in enumerate(tbl[0]):
        cnt[col_num] = 0
    for r in tbl:
        for col_num, c in enumerate(r):
            cnt[col_num] += 1
        
    return cnt
    
 
main()