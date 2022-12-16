#!/usr/bin/python3
# -*- coding: utf-8 -*-
# mushroom_name_generator.py

import os
import sys

root_fldr = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'rawdata'))
sys.path.insert(1, root_fldr)

import generate

op_fldr = generate.dat_fldr + os.sep
words = generate.get_list_words()
places = generate.get_list_places()

first_name = ['Glowing','Glowing','Lumin','Spotted', 'Silky', 'Slimy', 'Spotty','Jungle', 'Northern', 'Southern', 'Western', 'Eastern', 'Forest', 'Poison']
 
name_start = ['Yellow', 'Blue', 'Red', 'Dark', 'Night',  'Soft', 'Spore', 'Dark']
 
#name_end = ['Mushroom', 'Truffle', 'Deathcap', 'Suncap', 'Fungi', 'Shroom', 'Belltop', 'Spore', 'Toadstool']
name_end = ['shroom', 'shroom', 'shroom',  'cap',  'cap', 'top', 'cap',  'fungi', 'top', 'spore', 'bane']

gen_res = generate.TableGenerator(6000000, [first_name, name_start, name_end], ['first_name', 'Name_start', 'name_end'])
dist_list = []
for row in gen_res.tbl:
    if row not in dist_list:
        if row != []:
            dist_list.append(row)

for dst in dist_list:
    print(dst[0] + ' ' + dst[1] + '' + dst[2])

print('Distinct names = ' + str(len(dist_list)))   # 638 names (probably max) if 100,000 generated randomly