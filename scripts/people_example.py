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
    
def make_random_set_of_persons(num_persons=5):    
    s = content.Samples(root_path)
    person_generator = s.get_sample_by_name('person_consumer')
    persons = []
    for n in range(num_persons):
        persons.append(random_person(person_generator))
    return persons
    
def random_person(person_generator):
    person = {}
    for l in person_generator.lists:
        for k,v in l.items():
            person[k] = random.choice(v)
    return person
    
    
main()