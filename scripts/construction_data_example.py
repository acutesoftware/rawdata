#!/usr/bin/python3
# coding: utf-8
# create_construction_data.py

import os
import sys

root_fldr = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'rawdata'))
sys.path.insert(1, root_fldr)

import generate
import errors
import content
import events

op_fldr = os.getcwd() + os.sep

s = content.DataFiles()

# define basic lists
file_actions = os.path.join(content.data_fldr,'building','actions.csv')
file_materials = os.path.join(content.data_fldr,'building','materials_common.csv')
file_workers = os.path.join(content.data_fldr,'building','workers.csv')

# generate list of workers
workers_table = generate.TableGenerator(4, ['PEOPLE', 'PEOPLE'], ['First Name', 'Surname'])
workers_table.save_table(file_workers)


# Create a Schedule of Work
for i in range(0, 12):
    worker = s.get_sample(file_workers, 'First Name')
    action = s.get_sample(file_actions, 'method')
    material = s.get_sample(file_materials, 'name')
    print( worker , 'will', action, 'the', material)
    

