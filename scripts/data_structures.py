#!/usr/bin/python3
# -*- coding: utf-8 -*-
# py_data01.py
# written by Duncan Murray 22/1/2025
# examples of python data structures

import random 
import pprint
raw_list_names = ['Frank', 'Susan', 'John', 'Mary']
raw_list_travel = ['Car', 'Skateboard', 'Plane', 'Boat', 'Bike']

def main():
    print('creating data structures...')
    make_grid()
    make_tuple()
    make_set()
    make_tree()
    make_dataclass()
    make_dict()
    #dummy()
    #make_default_dict()



def dummy():
    op = 'TODO'
    pprint.pprint(op)    

def make_default_dict():
    """
    Create a default dictionary
     {'Names': ['Frank', 'Susan', 'John', 'Mary'], 'Travel': ['Car', 'Skateboard', 'Plane', 'Boat', 'Bike']}
    """
    print('\nDefault Dict')
    from collections import defaultdict
    op = defaultdict(list)
    for nme in raw_list_names:
        op["Names"].append(nme)
    for trv in raw_list_travel:
        op["Travel"].append(trv)
    pprint.pprint(op) 

def make_grid():
    """
    Create a list of lists that acts as a grid
        [['Name', 'Car', 'Skateboard', 'Plane', 'Boat', 'Bike'],
        ['Frank', 'Y', 'N', 'N', 'N', 'N'],
        ['Susan', 'N', 'Y', 'N', 'N', 'Y'],
        ['John', 'Y', 'Y', 'Y', 'Y', 'Y'],
        ['Mary', 'Y', 'N', 'N', 'Y', 'N']]    
    """
    print('\nGrid - List of Lists')
    op = [['Name'] + raw_list_travel]
    for name in raw_list_names:
        row = [name] + [random.choice(['Y', 'N']) for _ in raw_list_travel]
        op.append(row)
    pprint.pprint(op)         

def make_tuple():
    """
    create a Tuple structure
    """
    print('\nTuple - read only (not used much anymore)')
    op = tuple(raw_list_travel)
    pprint.pprint(op)

def make_set():
    """
    create a Set structure
    """
    print('\nSet - unique list')
    op = set([t for t in raw_list_travel])
    pprint.pprint(op)


def make_tree():
    """
    create a tree structure
    """
    print('\nTree - there are no built in Tree data structures, see - https://stackoverflow.com/questions/2358045/how-can-i-implement-a-tree-in-python')

def make_dict():
    """
    make a simple dictionary
    """
    print('\nDictionary')
    op = { "name": random.choice(raw_list_names),
           "trav": random.choice(raw_list_travel)
        }
    
    pprint.pprint(op)


def make_dataclass():
    """
    create a tree structure
    """
    print('\nData Class')
    from dataclasses import dataclass
    @dataclass
    class FavTrav:
        name: str
        trav_type: str

    op = FavTrav(random.choice(raw_list_names), random.choice(raw_list_travel))

    pprint.pprint(op)

if __name__ == '__main__':
    main()
