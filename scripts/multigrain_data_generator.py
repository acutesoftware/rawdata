#!/usr/bin/python3
# coding: utf-8
# multigrain_data_generator.py
#
# This will generate  tables of similar data
# of different grains to test the aikif grain
# identifier 
#



import os
import sys

root_fldr = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'rawdata'))
sys.path.insert(1, root_fldr)

import generate
import errors
import content
import events

op_fldr = os.getcwd() + os.sep
years = [y for y in range(2010,2017)] #['2012', '2013', '2014', '2015', '2016', '2017']
workers = ['Fred', 'John', 'Mary', 'Jane', 'Julie', 'Justine', 'Bob', 'Joan', 'David', 'Cindy', 'Sue', 'Bill',
            'Maude', 'Jim', 'James', 'Ethyl', 'Raj', 'Eric','Santos' ]
projects = ['60' + str(n) for n in range(1000,9990, 313)]
customer_rating = [y for y in range(1,6)]

def main():

    # Table 1 - grain_project_person_year.csv
    # has one record for every person in every project per year

    colLabel = ['DATE', 'Project Code', 'Location',  'Contractor', 'Balance', 'Customer Rating']
    colTypes = [years, projects, 'PLACE', workers, 'CURRENCY', customer_rating]
    tbl = generate.TableGenerator(2000, colTypes, colLabel)
    tbl.save_table('grain_person_project_year.csv')


    colLabel1 = ['DATE', 'Contractor',  'Num Jobs', 'Total Amount']
    tbl_agg_1 = agg_1(tbl, colLabel1)
    save_table(tbl_agg_1, colLabel1, 'grain_person_year.csv')

    colLabel2 = ['Contractor',  'Num Jobs', 'Total Amount', 'Avg Rating']
    tbl_agg_2 = agg_2(tbl, colLabel2)
    save_table(tbl_agg_2, colLabel2, 'grain_person.csv')

    colLabel3 = ['DATE',  'Total Amount']
    tbl_agg_3 = agg_3(tbl, colLabel3)
    save_table(tbl_agg_3, colLabel3, 'grain_year.csv')

    colLabel4 = ['Contractor',  'Location', 'Total Amount']
    tbl_agg_4 = agg_4(tbl, colLabel4)
    save_table(tbl_agg_4, colLabel4, 'grain_person_location.csv')

    
def agg_1(tbl, colLabel):    
    # Table 2 - grain_person_year.csv
    # has one record for every person per year
    tbl_agg = []
    for row_worker in workers:
        for row_year in years:
            amt = 0
            num_jobs = 0
            for r in tbl.tbl:
                if r[0] == row_year:
                    if r[3] == row_worker:
                        num_jobs += 1
                        amt += get_num_from_curr(r[4])
            tbl_agg.append([row_year, row_worker, num_jobs, amt])
    return tbl_agg
            
def agg_2(tbl, colLabel):    
    # Table 2 - grain_person_year.csv
    # has one record for every person per year
    tbl_agg = []
    for row_worker in workers:
        amt = 0
        num_jobs = 0
        tot_rating = 0
        for r in tbl.tbl:
            if r[3] == row_worker:
                num_jobs += 1
                amt += get_num_from_curr(r[4])
                tot_rating += r[5]
        tbl_agg.append([row_worker, num_jobs, amt, tot_rating/num_jobs])
    return tbl_agg
            
def agg_3(tbl, colLabel):    
    # Table 3 - grain_year.csv
    # has one record for every year
    tbl_agg = []
    for row_year in years:
        amt = 0
        for r in tbl.tbl:
            if r[0] == row_year:
                    amt += get_num_from_curr(r[4])
        tbl_agg.append([row_year, amt])
    return tbl_agg
 
def agg_4(tbl, colLabel):    
    # Table 4 - grain_person_location.csv
    tbl_agg = []
    
    # first get distinct list of locations from source data
    locations = list(set([r[2] for r in tbl.tbl]))
    #print(locations)
    
    
    # do the aggregate
    for row_worker in workers:
        for row_loc in locations:
            amt = 0
            for r in tbl.tbl:
                if r[3] == row_worker:
                    if r[2] == row_loc:
                        amt += get_num_from_curr(r[4])
            tbl_agg.append([row_worker, row_loc, amt])
    return tbl_agg
 
    

def get_num_from_curr(raw_val):
    """
    strips the random currency generation and returns a value
    """
    op_str = raw_val.strip('+').strip(',').strip(' ').strip('$')
    return float(op_str)
    

def save_table(tbl, hdr, fname, delim=',', qu='"'):
    with open(fname, "wt") as f:
        f.write(delim.join([qu + col + qu for col in hdr]) + '\n')
        f.write('\n'.join(delim.join([qu + col + qu if type(col) is str else qu + str(col) + qu for col in row]) for row in tbl))    

main()

