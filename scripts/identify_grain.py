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
    dual_col_counts = get_dual_col_counts(tbl)
    #print(dual_col_counts)
    for k,v in dual_col_counts.items():
        #print(k,v)
        if v == num_rows:
            #print('Grain match!')
            grain += '\ndual col: ' + k + '  '
    
    
    if grain == '':
        grain = 'Not sure  '

    return grain[:-2]  # trim last 2 chars for trailing commas in mult cols
    
def get_counts_by_col(tbl):
    """
    get counts by single column of a table
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
 
 
 
def get_dual_col_counts(tbl):
    """
    get counts by 2 cols of a table
        Grain of grain_year.csv is :  DATE, Total Amount,
        dual col: DATE,Total Amount
        dual col: Total Amount,DATE
        Grain of grain_person_location.csv is :
        dual col: Contractor,Location
        dual col: Location,Contractor    
    """
    cnt = {}
    col_vals = {}
    #print('get_counts_by_col(tbl)  = ', tbl[0:5])
    for col_num1, c1 in enumerate(tbl[0]):
        for col_num2, c2 in enumerate(tbl[0]):
            if col_num1 != col_num2:
                col_vals[tbl[0][col_num1] + ',' + tbl[0][col_num2]] = get_unique_vals2(tbl, col_num1,col_num2)
                cnt[tbl[0][col_num1] + ',' + tbl[0][col_num2]] = len(col_vals[tbl[0][col_num1] + ',' + tbl[0][col_num2]])
                
    return cnt
 
def get_unique_vals2(tbl, col_num1, col_num2):
    """
    returns a set of unique values in col_num of tbl
    """
    vals = []
    for r in tbl[1:]:
        vals.append(r[col_num1] + r[col_num2] )
    return list(set(vals))
 
 
 
main()