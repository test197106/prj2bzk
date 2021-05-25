

import sys
from pathlib import Path
import importlib
import requests
import json
import re


def fn_get_values():
    fn_get_user_par()
    fn_get_settings()
    fn_get_prog_par()


def fn_get_user_par():
    global di_u
    e = '=================================================================================='
    print(e+'\nKeys & its values of dictionary : gv.di_u\n'+e)
    for x,y in sorted(di_u.items()):
        print(" gv.di_u['"+x+"'] = '"+str(y)+"'")
    print(e,end='\n\n')


def fn_get_settings():
    global di_s
    e = '=================================================================================='
    print(e+'\nKeys & its values of dictionary : gv.di_s\n'+e)
    for x,y in sorted(di_s.items()):
        print(" gv.di_s['"+x+"'] = '"+str(y)+"'")
    print(e,end='\n\n')


def fn_get_prog_par():
    global di_p
    e = '=================================================================================='
    print(e+'\nKeys & its values of dictionary : gv.di_p\n'+e)
    for x,y in sorted(di_p.items()):
        print(" gv.di_p['"+x+"'] = '"+str(y)+"'")
    print(e,end='\n\n')


def fn_get_functions():
    # Get global functions of this module
    e = '=================================================================================='
    print(e+'\nFunctions of module: gv\n'+e)
    for x in sorted(globals()):
        if x.startswith('fn_'):
            print('gv.'+x)
    print(e,end='\n\n')


def fn_get_vars():
    # Get global variables of this module
    m = [ 'sys', 'Path', 'importlib', 'requests', 'json', 're'  ]
    e = '=================================================================================='
    print(e+'\nVariables of module: gv\n'+e)
    for x in sorted(globals()):
        if x not in m and not x.startswith('_') and not x.startswith('fn_'):
            print('gv.'+x)
    print(e,end='\n\n')


def fn_takeover(h,b):
    # Taken over the control from previous function
    #print('Taken over!!',end='\n\n')
    fn_init_h(h)
    c0=str(b);j=Path(h['st_data_top_dir'])/h['st_proj_name'];
    k=j/h['st_proj_role'];d0=str(k);d1=str(j/'p1.BDI');
    d2=str(j/'p2.ETL');d3=str(j/'p3.EDA');
    d4=str(j/'p4.MDO');d5=str(j/'p5.MCU');
    d6=str(j/'p6.MPL');d7=str(j/'p7.RQI');
    if not j.exists(): j.mkdir(mode=0o700, parents=True, exist_ok=True)
    if not k.exists(): k.mkdir(mode=0o700, parents=True, exist_ok=True)
    fn_set_dirs(c0, d0, d1, d2, d3, d4, d5, d6, d7)
    #fn_get_vars()
    #fn_get_values()


def fn_reload():
    # Reload this module from python file
    x=importlib.reload(sys.modules['mypygvar'])
    y=str(x).replace('>','').replace("'","").split()[3]
    print('Reloaded functions from {}'.format(y))


def fn_ping():
    # Respond for ping requests from calling program
    print('I am alive!')


def fn_init():
# Initialize gv module
    global di_u
    global di_s
    global di_p
    try:
        x=type(di_u)
    except:
        di_u={}
        di_u['1s_valid']        = 'Y'
        di_u['st_code_top_dir'] = None
        di_u['st_data_top_dir'] = None
        di_u['st_proj_name']    = None
        di_u['st_proj_role']    = None
        di_u['st_git_user']     = None
        di_u['st_git_raw_url']  = None
    try:
        x=type(di_s)
    except:
        di_s={}
        di_s['1s_valid']        = 'Y'
        di_s['code_dir_0']     = None
        di_s['data_dir_0']     = None
        di_s['data_dir_1']     = None
        di_s['data_dir_2']     = None
        di_s['data_dir_3']     = None
        di_s['data_dir_4']     = None
        di_s['data_dir_5']     = None
        di_s['data_dir_6']     = None
        di_s['data_dir_7']     = None
    try:
        x=type(p)
    except:
        di_p={}
        di_p['1s_valid']        = 'Y'


def fn_init_h(di_name):
# Initialize gv module
    global di_u
    global di_s
    global di_p
    h=di_name
    try:
        x=type(h)
        j={}
        y=type(j)
        if not x == y:
            raise Exception("Only dictionary item can be given as input") 
    except:
        h={}
        h['1s_valid']     = 'Y'
        h['st_code_top_dir'] = None
        h['st_data_top_dir'] = None
        h['st_proj_name']    = None
        h['st_proj_role']    = None
        h['st_git_user']     = None
        h['st_git_raw_url']  = None
    try:
        x=type(di_u)
    except:
        di_u=h
    try:
        x=type(di_s)
    except:
        di_s={}
        di_s['1s_valid']     = 'Y'
        di_s['code_dir_0']  = None
        di_s['data_dir_0']  = None
        di_s['data_dir_1']  = None
        di_s['data_dir_2']  = None
        di_s['data_dir_3']  = None
        di_s['data_dir_4']  = None
        di_s['data_dir_5']  = None
        di_s['data_dir_6']  = None
        di_s['data_dir_7']  = None
    try:
        x=type(di_p)
    except:
        di_p={}
        di_p['1s_valid']     = 'Y'


def fn_set_dirs(c0, d0, d1, d2, d3, d4, d5, d6, d7):
# Safely set all directories used in this project
    global di_s
    fn_init()
    if di_s['code_dir_0'] == None: di_s['code_dir_0'] = c0
    if di_s['data_dir_0'] == None: di_s['data_dir_0'] = d0
    if di_s['data_dir_1'] == None: di_s['data_dir_1'] = d1
    if di_s['data_dir_2'] == None: di_s['data_dir_2'] = d2
    if di_s['data_dir_3'] == None: di_s['data_dir_3'] = d3
    if di_s['data_dir_4'] == None: di_s['data_dir_4'] = d4
    if di_s['data_dir_5'] == None: di_s['data_dir_5'] = d5
    if di_s['data_dir_6'] == None: di_s['data_dir_6'] = d6
    if di_s['data_dir_7'] == None: di_s['data_dir_7'] = d7


def fn_renew_dirs(c0, d0, d1, d2, d3, d4, d5, d6, d7):
# Forcefully set all directories used in this project
    global di_s
    fn_init()
    di_s['code_dir_0'] = c0
    di_s['data_dir_0'] = d0
    di_s['data_dir_1'] = d1
    di_s['data_dir_2'] = d2
    di_s['data_dir_3'] = d3
    di_s['data_dir_4'] = d4
    di_s['data_dir_5'] = d5
    di_s['data_dir_6'] = d6
    di_s['data_dir_7'] = d7


def fn_set_data_dir (i_dirname, i_dirvalue):
# Safely set a given directory used in this project
    global di_s
    fn_init()
    if di_s[i_dirname] == None:
        di_s[i_dirname] = i_dirvalue
        x='Value of Key:{} initialized to\n  {}'
        print(x.format(i_dirname,di_s[i_dirname]))


def fn_renew_data_dir (i_dirname, i_dirvalue):
# Forcefully set a given directory used in this project
    global di_s
    fn_init()
    di_s[i_dirname] = i_dirvalue
    x='Value of Key:{} reset to\n  {}'
    print(x.format(i_dirname,di_s[i_dirname]))


def fn_restore_dict(i_diname, i_fname, i_obj):
    a=Path(di_s['data_dir_0'])/i_fname
    p=re.compile('(?<!\\\\)\'')
    o_obj=i_obj
    if a.exists():
        with open(a,'rt') as f:
            d = f.read()
            e = p.sub('\"', d)
        m_obj = json.loads(e)
        o_obj.update(m_obj)
        print('Dictionary gv.{} restored and refreshed'.format(i_diname))
    else:
        print('Dictionary gv.{} unchanged'.format(i_diname))
    return o_obj


# Regex code extracted from following URL
# https://stackoverflow.com/questions/39491420/python-jsonexpecting-property-name-enclosed-in-double-quotes
def fn_refresh_dict(i_diname, i_fname, i_obj):
    a=Path(di_s['data_dir_0'])/i_fname
    p=re.compile('(?<!\\\\)\'')
    if a.exists():
        with open(a,'rt') as f:
            d = f.read()
            e = p.sub('\"', d)
        m_obj = json.loads(e)
        m_obj.update(i_obj)
        print('Dictionary gv.{} refreshed'.format(i_diname))
    else:
        m_obj = i_obj
        print('Dictionary gv.{} unchanged'.format(i_diname))
    return m_obj


def fn_save_dict(i_diname, i_fname, i_obj):
    a=Path(di_s['data_dir_0'])/i_fname
    with open(a,'wt') as f:
        print(i_obj,file=f)
    print('Saved gv.{} dictionary'.format(i_diname))


# Only one of three methods mentioned in the followig URL is implemented
# https://www.geeksforgeeks.org/how-to-read-dictionary-from-file-in-python/
# Other methods will be implemented later
def fn_refresh_settings():
    global di_s
    di_s=fn_refresh_dict('gv_di_s.txt',di_s)


def fn_save_settings():
    global di_s
    fn_save_dict('di_s','gv_di_s.txt',di_s)


def fn_restore_all_di():
    global di_u
    global di_s
    global di_p
    di_u=fn_restore_dict('di_u','gv_di_u.txt',di_u)
    di_s=fn_restore_dict('di_s','gv_di_s.txt',di_s)
    di_p=fn_restore_dict('di_p','gv_di_p.txt',di_p)


def fn_refresh_all_di():
    global di_u
    global di_s
    global di_p
    di_u=fn_refresh_dict('di_u','gv_di_u.txt',di_u)
    di_s=fn_refresh_dict('di_s','gv_di_s.txt',di_s)
    di_p=fn_refresh_dict('di_p','gv_di_p.txt',di_p)


def fn_save_all_di():
    global di_u
    global di_s
    global di_p
    fn_save_dict('di_u','gv_di_u.txt',di_u)
    fn_save_dict('di_s','gv_di_s.txt',di_s)
    fn_save_dict('di_s','gv_di_p.txt',di_p)


