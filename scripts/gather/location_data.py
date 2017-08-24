#!/usr/bin/python3
# -*- coding: utf-8 -*-
# location_data.py

import requests
import pprint
import os

root_fldr = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

fldr = os.path.join(root_fldr,'tests')

#src_file = os.path.join(fldr,'list_names_to_lookup.txt')
src_file = os.path.join(fldr,'list_names_to_lookup_CUT.txt')

if os.path.exists(src_file):
    lst = []
    with open(src_file, 'r') as f:
        for line in f:
            lst.append(line.strip('\n'))
else:
    lst = ['Glenelg Jetty', 
           'Sydney Opera House', 
           'Uluru', 
           'New York,Central Park',
           'Zimbabwe,Victoria Falls',
           '1 King William St, Adelaide, Australia',
           'Eiffel Tower',
           'Grand Canyon National Park',
           'Big Ben, London',
           'Kentucky Fried Chicken, Melbourne Central',
           'Mt Everest',
           '143 E Houston St, New York',
           'Ploshchad (Square)',
           'ABC, Perth'] 
     


base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

#raw_json_file = os.path.join(fldr,'json_raw.txt')
raw_json_file = os.path.join(os.getcwd(), 'json_raw.txt')
address_file = os.path.join(os.getcwd(), 'address.csv')


if os.path.exists(raw_json_file):
    os.remove(raw_json_file)
if os.path.exists(address_file):
    os.remove(address_file)

def main():
    res = '"search_term","result_num","gps_lat","gps_lng","formatted_address","country",\n'
    for name in lst:
        try:
            res += lookup_address(name)
        except Exception as ex:
            print('missing data for ', name)
    with open(address_file, 'w') as f:
        f.write(res)
    print('Done')

def lookup_address(nme):
    """
    use the Google map API to get address details
    """
    csv_line = ''        
    response = requests.get(base_url + 'address=' + nme)

    resp_json_payload = response.json()
    with open(raw_json_file, 'a') as f_raw:
        try:
            pprint.pprint(resp_json_payload, stream=f_raw)
        except Exception as ex:
            #print('Whoops - cant pprint this one: ' + str(ex))
            pass
    
    if len(resp_json_payload['results']) == 0:
        csv_line += '"' + nme + '",'        
        csv_line += '"0",\n'   
        return csv_line
        
    for result_num,result in enumerate(resp_json_payload['results']):
        csv_line += '"' + nme + '",'        
        csv_line += '"' + str(result_num+1) + '",'        
        for add in result['address_components']:
            if 'type' in add:
                if 'premise' in add['type']:
                    csv_line += '"' + add['short_name'] + '",'
                else:
                    csv_line += '",",'
                    
                if 'country' in add['type']:
                    csv_line += '"' + add['short_name'] + '",'
                else:
                    csv_line += '",",'
                    
        csv_line += '"' + str(result['geometry']['location']['lat']) + '",'
        csv_line += '"' + str(result['geometry']['location']['lng']) + '",'
        csv_line += '"' + result['formatted_address'] + '",'
        
        add_details = result['formatted_address'].split(',')
        csv_line += '"' + add_details[len(add_details)-1].strip(' ').upper() + '",'
        
        csv_line += '\n'            
    return csv_line
    
main()