#!/usr/bin/python3
# sys_PC_usage.py 

from win32gui import GetWindowText, GetForegroundWindow
import time

import rawdata.config as mod_cfg
op_folder = mod_cfg.fldrs['pers_data']

def get_user():
    """
    return the name of the user logged on to the PC
    """
    try:
        import getpass
        usr = getpass.getuser()
    except Exception:
        usr = 'username'
    return usr

def get_pc_name():
    """
    return the PC name (host / machine name)
    """
    try:
        import socket
        pcname = socket.gethostname()
    except Exception:
        pcname = 'computer'
    return pcname

fname = op_folder + 'pc_usage_' + get_pc_name() + '_' + get_user() + '.txt'


def main():
    """
    run in a loop and log the caption of the 
    active window every second. Save to disk
    each minute
    """
    lstRaw = []
    prevText = ''
    print('Logging PC usage to ' + fname)
    startTime = TodayAsString()
    tot_seconds = 1
    try:
        while True:
            txt = GetWindowText(GetForegroundWindow())
            if txt == prevText:
                tot_seconds = tot_seconds + 1
            else:
                lstRaw.append(startTime + ',' + format(tot_seconds, "03d") + ',' + txt)
                prevText = txt
                tot_seconds = 1
                startTime = TodayAsString()
            time.sleep(1)
            if TodayAsString()[-3:] == ':00':
                lstRaw.append(startTime + ',' + format(tot_seconds, "03d") + ',' + txt)
                #print('Recording data')
                tot_seconds = 1
                startTime = TodayAsString()
                record(lstRaw)
                lstRaw = []

    except KeyboardInterrupt:	
        print("logging halted")  
        # save the latest record
        lstRaw.append(startTime + ',' + format(tot_seconds, "03d") + ',' + txt) 
        record(lstRaw)
    
def TodayAsString():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def record(lst):
    with open(fname, "a") as f:
        for txt in lst:
            f.write(txt + '\n')
        
if __name__ == '__main__':
    main()
    
    
