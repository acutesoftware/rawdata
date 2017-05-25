#!/usr/bin/python3
# -*- coding: utf-8 -*-
# people_example.py

import os
import sys
import random
import pprint

root_fldr = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'rawdata'))
sys.path.insert(1, root_fldr)
root_path = root_fldr + os.sep + 'samples'

import generate
import content

def main():
    """
    generate a large number of people with random attributes
    """
    persons = make_random_set_of_persons(3)
    pprint.pprint(persons)
   
    # V2 - not working yet
    #workers = make_random_set_of_workers(5)
    #pprint.pprint(workers)
    
def make_random_set_of_persons(num_persons=5):    
    s = content.Samples(root_path)
    person_generator = s.get_sample_by_name('person_consumer')
    persons = []
    for n in range(num_persons):
        persons.append(random_person(person_generator))
    return persons
    
   
def make_random_set_of_workers(num_persons=5):    
    s = content.Samples(root_path)
    person_generator = s.get_sample_by_name('person_worker')
    persons = []
    print('person_generator = ', person_generator)
    for n in range(num_persons):
        persons.append(random_person_v2(person_generator))
    return persons
    
def random_person(person_generator):
    """ 
    original function 
    """
    person = {}
    for l in person_generator.lists:
        for k,v in l.items():
            person[k] = random.choice(v)
    return person
    
def random_person_v2(person_generator):
    """ 
    this should use the LISTS and the COLUMNS
    which the original function isnt doing - not there yet
    """
    person = {}
    custom_list = 'N'
    
    print('person_generator.col_labels = ', person_generator.col_labels)
    print('person_generator.col_types = ', person_generator.col_types)
    for num, l in enumerate(person_generator.col_labels):
        custom_list = 'N'
        if l in person_generator.lists:
                custom_list = 'Y'
    
    
        if custom_list == 'Y':
            print('custom list = ', person_generator.lists)
        if person_generator.col_types == 'NAME':
            print('getting name')
        elif person_generator.col_types == 'WORD':
            print('getting word')
        elif person_generator.col_types == 'PLACE':
            print('getting place')
        else:   # it is a list
            person[l] = random.choice(person_generator.col_types)
    return person
    
    
main()