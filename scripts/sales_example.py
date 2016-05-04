#!/usr/bin/python3
# -*- coding: utf-8 -*-
# sales_example.py

import os
import sys

root_fldr = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'rawdata'))
sys.path.insert(1, root_fldr)

import generate
import errors

def main():
    """
    generate a sales example with tables for customers,
    sales, products
    """
    date_list = generate.get_list_dates(2009, 2016)
    product_list = ['cabbage', 'online game', 'pencil', 'Milk', 'used car', 'plane ticket']
    tbl_sales = generate.TableGenerator(25, [date_list, 'PEOPLE', product_list, 'CURRENCY'], ['Date of sale', 'CustomerName', 'Product', 'Amount'])
    tbl_sales.save_table('sales.csv')
    

main()