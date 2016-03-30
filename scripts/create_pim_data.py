#!/usr/bin/python3
# create_pim_data.py

import os
import sys

root_fldr = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'rawdata'))
sys.path.insert(1, root_fldr)

import generate
import errors
import content
import events

op_fldr = generate.dat_fldr + os.sep
words = generate.get_list_words()
places = generate.get_list_places()

# Dairy
custom_event = ['Sales Meeting', 'Workshop', 'Training', 'Phone Hookup', 'Admin', 'Development work', 'Testing', 'Documentation']
tpe_event = ['DATE', 'PEOPLE', 'PLACE', custom_event ]
t_event = generate.TableGenerator(15,tpe_event, ['DATE', 'Name',   'Location', 'Details'])
t_event.save_table(op_fldr + 'diary.csv')

# Tasks
custom_task = ['Write report', 'fix bug', 'work on documentation', 'Add new feature', 'test new version', 'Demo to customer']
t_task = generate.TableGenerator(8, ['PEOPLE', ['Hi', 'Med', 'Low'], custom_task], ['Assigned to', 'Priority', 'Task'])
t_task.save_table(op_fldr + 'tasks.csv')

# Contacts
lbl_contact = ['Year_met', 'Customer_id', 'Age', 'First Name', 'Last Name', 'Country', 'Amount']
tpe_contact = ['DATE', 'STRING', 'INT', 'PEOPLE', 'PEOPLE', 'PLACE', 'CURRENCY']
t_contact = generate.TableGenerator(50, tpe_contact, lbl_contact)
t_contact.save_table(op_fldr + 'contacts.csv')

# test for new stuff
sample_dict = {'name' :'test_dict_by_weekday', 'scale':'day_of_week', 
               'trend':{'Mon':0.5, 'Tue':0.5, 'Wed':0.1, 'Thu':0.1, 'Fri':0.5}}

#sample_data = [['2016-03-01', 20], ['2016-04-22', 50]]
dates = ['2016-03-' + str(d) for d in range(1,31)]
sample_data = [[d, ndx] for ndx,d in enumerate(dates)]
print('BEFORE = ', sample_data)
t = events.TrendGenerator(sample_dict)
t.create_time_series(sample_data, 0, 1) 
print('AFTER = ', sample_data)


"""d = dict([(num + 335, round(0.14 + num*n,3)) 
                     for num, n in enumerate(
                      [0.14/25 for n in range(1, 25)])])
                      
                      
print(d)                      
"""
