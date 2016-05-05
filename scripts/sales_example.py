#!/usr/bin/python3
# -*- coding: utf-8 -*-
# sales_example.py

import os
import sys

root_fldr = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'rawdata'))
sys.path.insert(1, root_fldr)

import generate
import content

def main():
    """
    generate a sales example with tables for customers,
    sales, products
    """
    s = content.DataFiles()
    
    date_list = generate.get_list_dates(2016, 2016, 500)
    prod_list = list(s.get_collist_by_name(os.path.join(content.data_fldr,'food','garden_produce.csv'), 'name')[0])
    
    tbl_cust = generate.TableGenerator(8, ['STRING','PEOPLE', 'PEOPLE', 'PLACE'], ['Customer ID', 'First Name', 'Surname', 'Country'])
    tbl_cust.save_table('customers.csv')
    cust_list = list(s.get_collist_by_name('customers.csv', 'Customer ID')[0])
    
    tbl_sales = generate.TableGenerator(25, [date_list, cust_list, prod_list, 'CURRENCY'], ['Date of sale', 'Customer ID', 'Product', 'Amount'])
    tbl_sales.save_table('sales.csv')
 
main()