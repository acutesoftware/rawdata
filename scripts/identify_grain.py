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
    """
    Sample output with single column checks is below
    Grain of grain_person_year.csv is :  Total Amount
    Grain of grain_person_project_year.csv is :  Not sure
    Grain of grain_person.csv is :  Contractor, Total Amount
    Grain of grain_year.csv is :  DATE, Total Amount
    Grain of grain_person_location.csv is :  Not sure
    """
    for f in csv_files:
        res = identify_grain_csv(f)
        print('Grain of ' + f + ' is : ', res)
    
def load_to_array(name):
    """
    reads into list of lists - should use AIKIF cls_datatable
    """
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
    header_row = tbl[0]
    num_rows = len(tbl) - 1  # ignore the header

    #print('header = ', header_row)
    #print('num rows = ', num_rows)
     
    # check for single grain col
    col_counts = get_counts_by_col(tbl)
    for k,v in col_counts.items():
        #print(k,v)
        if v == num_rows:
            #print('Grain match!')
            grain += header_row[k] + ', '
    
    
    # check all combos here
    #dual_col_counts = get_dual_col_counts(tbl)
    
    if grain == '':
        grain = 'Not sure  '

    return grain[:-2]  # trim last 2 chars for trailing commas in mult cols
    
def get_counts_by_col(tbl):
    """
    get counts by all permutations of a table
    """
    cnt = {}
    col_vals = {}
    #print('get_counts_by_col(tbl)  = ', tbl[0:5])
    for col_num, c in enumerate(tbl[0]):
        col_vals[tbl[0][col_num]] = get_unique_vals(tbl, col_num)
        cnt[col_num] = len(col_vals[tbl[0][col_num]])
    return cnt
    
 
def get_unique_vals(tbl, col_num):
    """
    returns a set of unique values in col_num of tbl
    """
    vals = []
    for r in tbl[1:]:
        vals.append(r[col_num])
    return list(set(vals))
 
main()