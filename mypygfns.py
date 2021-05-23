# Define the bare minimum functions in the main section of this project
import mypygvar as gv
def gv_ping():
    print('I am alive!')
def fn_get_global_vars():
    x = [ 'In', 'Out', 'exit', 'get_ipython', 'quit',
         'sys', 'Path', 'importlib', 'requests' ]
    y = '========================='
    print(y+'\nGlobal Variable names\n'+y)
    for z in sorted(globals()):
        if z not in x and not z.startswith('_'): print(z)
    print()
def fn_get_gv_vars():
    x='========================='
    print(x+'\ngv Variable names\n'+x)
    for x in sorted(dir(gv)):
        if not x.startswith('_'): print(x)
    print()
def fn_get_ap_vars():
    x='========================='
    print(x+'\nap Variable names\n'+x)
    for x in sorted(dir(ap)):
        if not x.startswith('_'): print(x)
    print()
def gv_init():
# Initialize directory dictionary
    global di_dirs
    try:
        x=type(di_dirs)
    except:
        di_dirs={}
        di_dirs['code_dir_01'] = None
        di_dirs['data_dir_01'] = None
        di_dirs['data_dir_02'] = None
        di_dirs['data_dir_03'] = None
        di_dirs['data_dir_04'] = None
        di_dirs['data_dir_05'] = None
        di_dirs['data_dir_06'] = None
        di_dirs['data_dir_07'] = None
def gv_get_values():
## Get all directories used in this project
##   along with the project name and project role
    x='========================='
    print(x+'\ngv Values\n'+x)
    m='st_prjname = {}\nst_prjrole = {}'
    print(m.format(st_prjname,st_prjrole))
    print('di_dirs = ')
    for x,y in di_dirs.items():
        print(x+' : '+y)
    print()
def gv_set_dirs(c1, d1, d2, d3, d4, d5, d6, d7):
# Safely set all directories used in this project
    global di_dirs
    gv_init()
    if di_dirs['code_dir_01'] == None: di_dirs['code_dir_01'] = c1
    if di_dirs['data_dir_01'] == None: di_dirs['data_dir_01'] = d1
    if di_dirs['data_dir_02'] == None: di_dirs['data_dir_02'] = d2
    if di_dirs['data_dir_03'] == None: di_dirs['data_dir_03'] = d3
    if di_dirs['data_dir_04'] == None: di_dirs['data_dir_04'] = d4
    if di_dirs['data_dir_05'] == None: di_dirs['data_dir_05'] = d5
    if di_dirs['data_dir_06'] == None: di_dirs['data_dir_06'] = d6
    if di_dirs['data_dir_07'] == None: di_dirs['data_dir_07'] = d7
def gv_renew_dirs(c1, d1, d2, d3, d4, d5, d6, d7):
# Forcefully set all directories used in this project
    global di_dirs
    gv_init()
    di_dirs['code_dir_01'] = c1
    di_dirs['data_dir_01'] = d1
    di_dirs['data_dir_02'] = d2
    di_dirs['data_dir_03'] = d3
    di_dirs['data_dir_04'] = d4
    di_dirs['data_dir_05'] = d5
    di_dirs['data_dir_06'] = d6
    di_dirs['data_dir_07'] = d7
def gv_set_data_dir (i_dirname, i_dirvalue):
# Safely set a given directory used in this project
    global di_dirs
    gv_init()
    if di_dirs[i_dirname] == None:
        di_dirs[i_dirname] = i_dirvalue
        x='Value of Key:{} initialized to\n  {}'
        print(x.format(i_dirname,di_dirs[i_dirname]))
def gv_renew_data_dir (i_dirname, i_dirvalue):
# Forcefully set a given directory used in this project
    global di_dirs
    gv_init()
    di_dirs[i_dirname] = i_dirvalue
    x='Value of Key:{} reset to\n  {}'
    print(x.format(i_dirname,di_dirs[i_dirname]))
