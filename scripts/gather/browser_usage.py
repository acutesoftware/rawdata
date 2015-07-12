#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import time
import datetime
import sqlite3
import codecs
import json
import cgi
import urllib.parse as urlparse
from os.path import expanduser

import rawdata.config as mod_cfg

home = expanduser("~")
browser_data_path = home + r"\AppData\Local\Google\Chrome\User Data\Default" 
op_folder = mod_cfg.fldrs['pers_data']

#op_folder = 'sdgsdfsdgsdgsdg'
#browser_data_path = home + r"\FAKE_PATH_DOESNT_WORK\to_test_travis_ci" 

def TEST():
    """ self test for browser agent """
    browser = Browser(browser_data_path, op_folder, 'Chrome')
    browser.get_passwords()
    browser.get_browser_history_chrome()
    browser.get_browser_bookmarks_chrome()
    print(browser)

 
class Browser(object):
    """
    base class for browser
    """
    def __init__(self, browser_data_path, op_folder, name='Chrome', ):
        self.browser_data_path = browser_data_path
        self.op_folder = op_folder
        self.bookmarks_file = self.op_folder + os.sep + 'chrome_bookmarks.csv'
        self.history_file = self.op_folder + os.sep + 'chrome_history.csv'
        self.password_op = self.op_folder + os.sep + 'PASSWORDS.csv'
        self.num_bookmarks = 0
        self.num_folders = 0
        self.num_history = 0
        self.num_passwords = 0
        self.name = name
     
    def __str__(self):
        res = 'browser_usage reading ' + self.name + ' browser from datapath \n'
        res += '' + self.browser_data_path + '\n'
        res += 'Passwords        = ' + str(self.num_passwords) + '\n'
        res += 'History records  = ' + str(self.num_history) + '\n'
        res += 'Bookmarks        = ' + str(self.num_bookmarks) + '\n'
        res += 'Bookmark folders = ' + str(self.num_folders) + '\n'
        return res
        
    def DateConv(self, webkit_timestamp):
        return self.date_from_webkit(webkit_timestamp)
     
    def DateConvBookmark(self, webkit_timestamp):
        """
        DATE CONVERTER CHECK - input = 13027566429814640
        CONVERTING DATE
        days =  150782 seconds =  1629
        dte_as_date =  2013-10-30 00:27:09.814640
        2013-10-30 00:27:09        
        print('DateConvBookmark, INPUT = ', webkit_timestamp)
        """
        try:
            seconds, micros = divmod(webkit_timestamp, 1000000)
            days, seconds = divmod(seconds, 86400)
            dte_as_date = datetime.datetime(1601, 1, 1) + datetime.timedelta(days, seconds, micros)
            dte_as_str = str(dte_as_date)[0:19]    # for ISO standard date string yyyy-mm-dd hh:mm:ss
            #dte_as_str = dte_as_date.strftime( '%a, %d %B %Y %H:%M:%S %Z' )   # for long date string 
        except Exception:
            dte_as_str = ''
        return dte_as_str

    def date_from_webkit_ORIG_RETURNS_GMT_TIME(self, webkit_timestamp):
        epoch_start = datetime.datetime(1601,1,1)
        delta = datetime.timedelta(microseconds=int(webkit_timestamp))
        return epoch_start + delta
        
    def date_from_webkit(self, webkit_timestamp):
        UTC_OFFSET_TIMEDELTA = datetime.datetime.utcnow() - datetime.datetime.now()
        epoch_start = datetime.datetime(1601,1,1)
        delta = datetime.timedelta(microseconds=int(webkit_timestamp))
        return epoch_start + delta - UTC_OFFSET_TIMEDELTA

    def datetime_from_utc_to_local(self, utc_datetime):
        now_timestamp = time.time()
        offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
        return utc_datetime + offset

    def get_browser_bookmarks_chrome(self):
        """
        export Chrome bookmarks to CSV
        by reading Bookmarks file in json format
        """
        
        if not os.path.exists(self.browser_data_path):
            print('Cant find browser path to get bookmarks')
            return
        
        json_file = codecs.open(self.browser_data_path + os.sep + "Bookmarks", encoding='utf-8')
        bookmark_data = json.load(json_file)
        op = codecs.open(self.bookmarks_file, 'w', encoding='utf-8')
        op.write('"Full Folder","Title","URL","Date Added"\n')
        #print('exporting bookmarks...')
        
        def format_bookmark(base_folder, entry, delim = ',', qu='"'):
            """ 
            Extract fields into a formatted string 
            try:
                print('\n\nformat_bookmark = ', entry)
            except:
                print('cant export folder : ')
            """
            res = qu + base_folder + qu + delim
            res += qu + entry['name'] + qu + delim
            res += qu + cgi.escape(entry['url']) + qu + delim
            res += qu + self.DateConvBookmark(int(entry['date_added'])) + qu + delim
            res += qu + 'no date' + qu + delim
            return res + '\n'
            
        def format_bookmark_folder(base_folder, entry, delim = ',', qu='"'):
            """ 
            extract fields into a formatted string 
            """
            res = qu + base_folder + qu + delim
            try:
                res += qu + str(entry['name']) + qu + delim
            except Exception:
                res += qu + str(entry) + qu + delim  # first entry is string bookmark_bar
                
            # print dummy empty entry name because this is a folder, not a bookmark
            res += qu + 'Folder' + qu + delim
            try:
                res += qu + self.DateConvBookmark(entry['date_added']) + qu + delim
            except Exception:
                res += qu + '' + qu + delim  # may not be a dict, so no indexes 
            return res + '\n'
        
        def get_bookmarks(fldr, base_folder):
            """ 
            recursively get all bookmarks in fldr 
            """
            for entry in fldr:
                if entry['type'] == 'folder':
                    self.num_folders += 1
                    if len(entry['children']) > 0:
                        op.write(format_bookmark_folder(base_folder, entry))
                        if entry['children']:
                            next_folder = entry['children']
                            get_bookmarks(next_folder, base_folder + ':' + entry['name'])
                else:
                    self.num_bookmarks += 1
                    op.write(format_bookmark(base_folder, entry))
                    
        roots = bookmark_data['roots']

        for entry in roots:
            op.write(format_bookmark_folder('ROOT', entry))
            try:
                get_bookmarks(roots[entry]['children'], 'ROOT:')
                self.num_folders += 1
            except Exception:
                pass
            self.num_folders += 1
            
        op.close()     
        

    def get_browser_history_chrome(self):
        """
        export Chrome browser history to CSV 
        by reading the SQLite3 database
        """
        paths = [browser_data_path + "\\History"] 
        #pattern = "(((http)|(https))(://)(www.)|().*?)\.[a-z]*/"
        SQL_STATEMENT = 'SELECT '
        SQL_STATEMENT += 'urls.url, urls.title, urls.visit_count, urls.typed_count, urls.last_visit_time, '
        SQL_STATEMENT += 'visits.visit_time, urls.hidden, visits.from_visit, urls.id, visits.transition '
        SQL_STATEMENT += 'FROM urls, visits '
        SQL_STATEMENT += 'WHERE urls.id = visits.url;'
        
        self.num_history = 0
        
        try:
            storage = codecs.open(self.history_file, 'w', 'utf-8')
            storage.write('"url","visit_count","typed_count","last_visit_time","visit_time","hidden","from_visit","id","transition","title"\n')
        except Exception:
            print('Error - cant open history file for writing')
            
        try:
            for path in paths:
                c = sqlite3.connect(path)
                for row in c.execute(SQL_STATEMENT):
                    #storage.write( row[0] + ", " + row[1] + ", " + str(row[2])+ ", ")
                    storage.write(self.format_history_row(row))
                    self.num_history += 1
                    #date_time = date_from_webkit(row[1])
                    #url = re.search(pattern, row[0])
                    #try: urlc = url.group(0)
                    #except: urlc = "ERROR"
                    #storage.write(str(date_time)[0:19] + "\t" + urlc + "\n")
            #print('Exported ' + str(self.num_history) + ' records to ' + self.history_file)		
        except Exception:
            print('Error - cant open browser files - close Chrome and retry')
            

    def format_history_row(self, row):
        """
        format a chrome bookmark for csv
        """
        txt = '"'
        txt += row[0] + '","' 
        txt += str(row[2]) + '","'
        txt += str(row[3]) + '","'
        txt += str(self.DateConv(row[4]))[0:21]  + '","'
        txt += str(self.DateConv(row[5]))[0:21] + '","'
        txt += str(row[6]) + '","'
        txt += str(row[7]) + '","'
        txt += str(row[8]) + '","'
        txt += str(row[9]) + '","'
        txt += row[1] + '"\n'
        return txt
        
    def get_passwords(self):
        """
        exports the logins and passwords from Chrome
        """
        if not os.path.exists(self.op_folder):
            print('op folder doesnt exist')
            return
        
        try:
            db = sqlite3.connect(browser_data_path + os.sep + "Login Data")
            c = db.cursor()
            c.execute("SELECT * FROM logins WHERE blacklisted_by_user = 0")
            raw_password_data = c.fetchall()
            c.close()
            db.close()
        except Exception:
            raw_password_data = ''
        # export
        line = ''
        #print(raw_password_data)
        with open(self.password_op, "w") as f:
            f.write('"website","username","form_url","user_field","pass_field","password",\n')
            for row in raw_password_data:
                if row:
                    line = self.extract_password_row(row)
                    if line:
                        f.write(line)
        
        
        
         
    def extract_password_row(self, row):
        res = ''
        hostname_split = urlparse.urlsplit(row[0])
        website = urlparse.urlunsplit((hostname_split.scheme, hostname_split.netloc, "", "", "")).strip('\n')
        username = ''
        password = ''
        form_url = ''
        user_field = ''
        pass_field = ''
        form_url_split = urlparse.urlsplit(row[1])
        form_url = urlparse.urlunsplit((form_url_split.scheme, form_url_split.netloc, "", "", "")).strip('\n')
        #print('\nusername = ', row[3], ' password RAW = ', row[5])
        password = self.decode_password(row[5])
        try:
            username = row[3]
            try:
                password = self.decode_password(row[5])
                self.num_passwords += 1
            except Exception:
                print('ERROR - password = ', row[5])
            
            user_field = row[2]
            pass_field = row[4]
        except Exception:
            print('non password entry (blacklists - ignoring)')
        res = self.format_list_csv([website, username, form_url, user_field, pass_field, password])
        return res

        
    def decode_password(self, raw):
        """ 
        password from Chrome as byte arrays 
        Doesn't decode password, though tried several methods
        """
        #print("RAW = ", str(raw))
        v1 = str(raw)
        #  v2 = base64.b64decode("".join(b for b in raw))

        #password = "".join(map(chr, row[5]))
        #password = row[5].decode("windows-1252")
        #password = "".join( chr( val ) for val in row[5] )
        #import binascii
        #btes = [b for b in raw]
        #v3 = ' '.join(str(b) for b in btes)
        
        
        #v4 = ''
        #for b in raw:
        #    if b > 32 and b < 112:
        #        v4 += chr(int(b)) + ''
        
        res = v1
        #print("OP  = ", res)
        
        return res 
        
    def format_list_csv(self, lst, qu='"',delim=','):
        """
        takes a list of strings and converts to CSV
        """
        res = ''
        for l in lst:
            if l:
                res += qu + str(l) + qu + delim
            else:
                res += qu + '' + qu + delim
        res += '\n'
        return res
    
if __name__ == '__main__':
    TEST()  
