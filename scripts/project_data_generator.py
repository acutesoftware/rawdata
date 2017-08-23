#!/usr/bin/python3
# coding: utf-8
# project_data_generator.py

import os
import sys

root_fldr = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'rawdata'))
sys.path.insert(1, root_fldr)

import generate

op_fldr = os.getcwd() + os.sep
years = ['2012', '2013', '2014', '2015', '2016', '2017']
workers = ['Fred', 'John', 'Mary', 'Jane', 'Julie', 'Justine', 'Bob', 'Joan', 'David', 'Cindy', 'Sue', 'Bill',
            'Maude', 'Jim', 'James', 'Ethyl', 'Raj', 'Eric','Santos' ]
paint = ['Blue', 'Green', 'Orange', 'Yellow', 'Red']
locations = ['Africa', 'Australia', 'America', 'Asia']
projects = ['80' + str(n) for n in range(1000,79990)]

colLabel = ['DATE', 'Project Code', 'Location',  'Contractor', ' Job Colour',  'Balance']
colTypes = [years, projects, locations, workers, paint, 'CURRENCY']



tbl = generate.TableGenerator(9999, colTypes, colLabel)
tbl.save_table('random_projects.csv')
print(tbl)