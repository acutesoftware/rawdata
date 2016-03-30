#!/usr/bin/python3
# create_pim_data.py

import os
import sys

root_fldr = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'rawdata'))
sys.path.insert(1, root_fldr)

import generate
import errors
import content


op_fldr = generate.dat_fldr + os.sep
words = generate.get_list_words()
places = generate.get_list_places()

# Dairy
custom_event = ['Sales Meeting', 'Workshop', 'Training']
tpe_event = ['DATE', 'PEOPLE', 'PLACE', custom_event ]
t_event = generate.TableGenerator(15,tpe_event, ['DATE', 'Name',   'Location', 'Details'])
t_event.save_table(op_fldr + 'diary.csv')

# Tasks
custom_task = ['Write report', 'fix bug', 'work on documentation']
t_task = generate.TableGenerator(8, ['PEOPLE', 'INT', custom_task], ['Assigned to', 'Priority', 'Task'])
t_task.save_table(op_fldr + 'tasks.csv')

# Contacts
lbl_contact = ['Year_met', 'Customer_id', 'Age', 'Name', 'Country', 'Details', 'Amount']
tpe_contact = ['DATE', 'STRING', 'INT', 'PEOPLE', 'PLACE', 'WORD', 'CURRENCY']
t_contact = generate.TableGenerator(50, tpe_contact, lbl_contact)
t_contact.save_table(op_fldr + 'contacts.csv')

