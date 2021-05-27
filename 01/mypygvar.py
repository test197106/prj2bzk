

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
        t=type(y); m=" gv.di_u['"+x+"'] ="
        if t == type(''): print(m+" '"+y+"'")
        elif (t==type(1) or t==type(1.0) or t==type(True) or t==type(None)):
            print(m+" "+str(y))
        elif t == type(Path.home()): print(m+" Path('"+str(y)+"')")
        else: print(m+" Unknown('"+str(y)+"')")
    print(e,end='\n\n')


def fn_get_settings():
    global di_s
    e = '=================================================================================='
    print(e+'\nKeys & its values of dictionary : gv.di_s\n'+e)
    for x,y in sorted(di_s.items()):
        t=type(y); m=" gv.di_s['"+x+"'] ="
        if t == type(''): print(m+" '"+y+"'")
        elif (t==type(1) or t==type(1.0) or t==type(True) or t==type(None)):
            print(m+" "+str(y))
        elif t == type(Path.home()): print(m+" Path('"+str(y)+"')")
        else: print(m+" Unknown('"+str(y)+"')")
    print(e,end='\n\n')


def fn_get_prog_par():
    global di_p
    e = '=================================================================================='
    print(e+'\nKeys & its values of dictionary : gv.di_p\n'+e)
    for x,y in sorted(di_p.items()):
        t=type(y); m=" gv.di_p['"+x+"'] ="
        if t == type(''): print(m+" '"+y+"'")
        elif (t==type(1) or t==type(1.0) or t==type(True) or t==type(None)):
            print(m+" "+str(y))
        elif t == type(Path.home()): print(m+" Path('"+str(y)+"')")
        else: print(m+" Unknown('"+str(y)+"')")
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


def fn_takeover(h,k):
    # Taken over the control from previous function
    #print('Taken over!!',end='\n\n')
    fn_init_h(h)
    c1=str(k)
    fn_set_code_dirs(c1)
    fn_dnl_addl_mods()


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
        di_u[ '1s_valid'       ] = 'Y'
        di_u[ 'st_git_raw_url' ] = None
        di_u[ 'st_git_user'    ] = None
        di_u[ 'st_proj_name'   ] = None
        di_u[ 'st_proj_role'   ] = None
        di_u[ 'st_proj_vers'   ] = None
        di_u[ 'st_code_top_1'  ] = None
        di_u[ 'st_data_top_1'  ] = None
        di_u[ 'st_data_top_2'  ] = None
        di_u[ 'st_data_top_3'  ] = None
        di_u[ 'st_data_top_4'  ] = None
        di_u[ 'st_data_top_5'  ] = None
        di_u[ 'st_data_top_6'  ] = None
        di_u[ 'st_data_top_7'  ] = None
    try:
        x=type(di_s)
    except:
        di_s={}
        di_s['1s_valid']         = 'Y'
        di_s['st_code_dir_1']    = None
        di_s['st_data_dir_1']    = None
        di_s['st_data_dir_2']    = None
        di_s['st_data_dir_3']    = None
        di_s['st_data_dir_4']    = None
        di_s['st_data_dir_5']    = None
        di_s['st_data_dir_6']    = None
        di_s['st_data_dir_7']    = None
    try:
        x=type(p)
    except:
        di_p={}
        di_p['1s_valid']         = 'Y'


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
        h[ '1s_valid'       ] = 'Y'
        h[ 'st_git_raw_url' ] = None
        h[ 'st_git_user'    ] = None
        h[ 'st_proj_name'   ] = None
        h[ 'st_proj_role'   ] = None
        h[ 'st_proj_vers'   ] = None
        h[ 'st_code_top_1'  ] = None
        h[ 'st_data_top_1'  ] = None
        h[ 'st_data_top_2'  ] = None
        h[ 'st_data_top_3'  ] = None
        h[ 'st_data_top_4'  ] = None
        h[ 'st_data_top_5'  ] = None
        h[ 'st_data_top_6'  ] = None
        h[ 'st_data_top_7'  ] = None
    else:
        h[ 'st_data_top_1'  ] = None
        h[ 'st_data_top_2'  ] = None
        h[ 'st_data_top_3'  ] = None
        h[ 'st_data_top_4'  ] = None
        h[ 'st_data_top_5'  ] = None
        h[ 'st_data_top_6'  ] = None
        h[ 'st_data_top_7'  ] = None
    try:
        x=type(di_u)
    except:
        di_u=h
    try:
        x=type(di_s)
    except:
        di_s={}
        di_s['1s_valid'  ]       = 'Y'
        di_s['st_code_dir_1']    = None
        di_s['st_data_dir_1']    = None
        di_s['st_data_dir_2']    = None
        di_s['st_data_dir_3']    = None
        di_s['st_data_dir_4']    = None
        di_s['st_data_dir_5']    = None
        di_s['st_data_dir_6']    = None
        di_s['st_data_dir_7']    = None
    try:
        x=type(di_p)
    except:
        di_p={}
        di_p['1s_valid']     = 'Y'


def fn_set_code_dirs(c1):
# Safely set all code directories used in this project
    global di_s
    fn_init()
    if di_s['st_code_dir_1'] == None: di_s['st_code_dir_1'] = c1

def fn_renew_code_dirs(c1):
# Forcefully set all code directories used in this project
    global di_s
    fn_init()
    di_s['st_code_dir_1'] = c1

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
    a=Path(di_s['st_code_dir_1'])/i_fname
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
    a=Path(di_s['st_code_dir_1'])/i_fname
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


def fn_upd_data_dirs():
    global di_s
    fn_init()
    fli_1=[]
    #fli_2=[ 'p0.NON','p1.BDI','p2.ETL','p3.EDA',
    #        'p4.MDO','p5.MCU','p6.MPL','p7.RQI']
    fli_2=[ 'p0','p1','p2','p3',
            'p4','p5','p6','p7']
    global di_s
    fn_init()
    n=di_u['st_proj_name']
    r=di_u['st_proj_role']
    v=di_u['st_proj_vers']
    for x,y in di_u.items():
        if x.startswith('st_data_top_'):
            fli_1.append(y)
    for x in sorted(set(fli_1)):
        y=Path(x)
        if not y.exists():
            y.mkdir(mode=0o755, parents=True, exist_ok=True)
            print('Created following directory\n{}'.format(x))
    #for i in range(1,8):
    #    x='st_data_top_'+str(i)
    #    y=di_u[x]
    #    a=Path(y)/n
    #    if not a.exists(): a.mkdir(mode=0o755, parents=True, exist_ok=True)
    for i in range(1,8):
        x='st_data_top_'+str(i)
        y='st_data_dir_'+str(i)
        z=Path(di_u[x])/fli_2[i]
        if not z.exists(): z.mkdir(mode=0o755, parents=True, exist_ok=True)
        if di_s[y] == None: di_s[y]=str(z)


def fn_update_data():
    # Following entries can be modified by advanced users
    # For normal users please leave the entries below to its default values
    di_u['st_data_top_2'] = di_u['st_data_top_1']
    di_u['st_data_top_3'] = di_u['st_data_top_1']
    di_u['st_data_top_4'] = di_u['st_data_top_1']
    di_u['st_data_top_5'] = di_u['st_data_top_1']
    di_u['st_data_top_6'] = di_u['st_data_top_1']
    di_u['st_data_top_7'] = di_u['st_data_top_1']
    fn_upd_data_dirs()


def fn_dnl_addl_mods():
    li_1= [ 'allpyfns.py', 'allspmsg.csv', 'allspmsg.txt',
            'allsqcmd.csv', 'allsqcmd.sql' ]
    for f in li_1:
        g=di_u['st_git_raw_url'];
        u=di_u['st_git_user'];
        n=di_u['st_proj_name'];
        r=di_u['st_proj_role'];
        v=di_u['st_proj_vers'];
        k=di_s['st_code_dir_1']
        x=Path(k)/f;
        y=g+'/'+u+'/'+n+'/'+r+'/'+v+'/'+f
        if not x.exists(): x.write_bytes(requests.get(y, allow_redirects=True).content)


#def fn_set_data_dirs(c0, d0, d1, d2, d3, d4, d5, d6, d7):
## Safely set all directories used in this project
#    global di_s
#    fn_init()
#    if di_s['data_dir_1'] == None: di_s['data_dir_1'] = d1
#    if di_s['data_dir_2'] == None: di_s['data_dir_2'] = d2
#    if di_s['data_dir_3'] == None: di_s['data_dir_3'] = d3
#    if di_s['data_dir_4'] == None: di_s['data_dir_4'] = d4
#    if di_s['data_dir_5'] == None: di_s['data_dir_5'] = d5
#    if di_s['data_dir_6'] == None: di_s['data_dir_6'] = d6
#    if di_s['data_dir_7'] == None: di_s['data_dir_7'] = d7
#
#
#def fn_renew_data_dirs(c0, d0, d1, d2, d3, d4, d5, d6, d7):
## Forcefully set all directories used in this project
#    global di_s
#    fn_init()
#    di_s['data_dir_1'] = d1
#    di_s['data_dir_2'] = d2
#    di_s['data_dir_3'] = d3
#    di_s['data_dir_4'] = d4
#    di_s['data_dir_5'] = d5
#    di_s['data_dir_6'] = d6
#    di_s['data_dir_7'] = d7

