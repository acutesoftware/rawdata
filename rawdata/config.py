#!/usr/bin/python3
# -*- coding: utf-8 -*-
# config.py     

import os

fldrs = {}
logs = {}
params = {}

# path for personal data location  (TODO - you need to modify this line below!)

pers_fldr = 'T:\\user\\AIKIF'

fldrs['localPath'] = pers_fldr + os.sep 
fldrs['log_folder'] = pers_fldr + os.sep + 'log' 
fldrs['pers_data'] = pers_fldr + os.sep + 'pers_data' 
fldrs['pers_credentials'] = pers_fldr + os.sep + 'pers_data' + os.sep + 'credentials' 

# FOR DEVELOPMENT
core_folder = 'T:\\user\\dev\\src\\python\\AIKIF'
fldrs['root_path'] = core_folder
fldrs['public_data_path'] = core_folder + os.sep + 'data'
fldrs['program_path'] = os.path.abspath(core_folder + os.sep + 'aikif') 

# user defined parameters 
params['rawdata_version'] = '0.0.9'
params['rawdata_deploy'] = 'DEV'

