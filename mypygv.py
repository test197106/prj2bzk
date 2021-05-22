

# ====================================================
# Following dataypes are supported by this package
# Any other objects or object types will not be 
# supported by this package
#
# Text Type: 	        str
# Numeric Types: 	int, float, complex
# Sequence Types: 	list, tuple, range
# Mapping Type: 	dict
# Set Types: 	        set, frozenset
# Boolean Type: 	bool
# Binary Types: 	bytes, bytearray, memoryview
#
# ====================================================

def fn_init():
# Initialize important variables
    global st_prjname
    global st_prjrole
    global di_dirs
    try:
        x=type(st_prjname)
    except:
        st_prjname = None
    try:
        x=type(st_prjrole)
    except:
        st_prjrole = None
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
        di_dirs['data_dir_08'] = None
        di_dirs['data_dir_09'] = None
        di_dirs['data_dir_10'] = None
def fn_set_nrcvals(i_prjname, i_prjrole, i_codedir, i_mode='safe'):
    global st_prjname
    global st_prjrole
    global di_dirs
    fn_init()
    r='N'
    if i_mode == 'safe':
        r='Y'
        if st_prjname == None:
            st_prjname = i_prjname
            x='String:st_prjname initialized to {}'
            print(x.format(st_prjname))
        if st_prjrole == None:
            st_prjrole = i_prjrole
            x='String:st_prjrole initialized to {}'
            print(x.format(st_prjrole))
        if di_dirs['code_dir_01'] == None:
            di_dirs['code_dir_01'] = i_codedir
            x='Value of Key:code_dir_01 initialized to\n  {}'
            print(x.format(di_dirs['code_dir_01']))
    if i_mode == 'force':
        r='Y'
        st_prjname = i_prjname
        x='String:st_prjname reset to {}'
        print(x.format(st_prjname))
        st_prjrole = i_prjrole
        x='String:st_prjrole reset to {}'
        print(x.format(st_prjrole))
        di_dirs['code_dir_01'] = i_codedir
        x='Value of Key:code_dir_01 reset to\n  {}'
        print(x.format(di_dirs['code_dir_01']))
    if r != 'Y':
        print('Valid modes are listed below:\n  safe  force')
        print('Default mode: safe')
def fn_get_allvals():
    x='========================='
    print(x+'\ngv Values\n'+x)
    m='st_prjname = {}\nst_prjrole = {}'
    print(m.format(st_prjname,st_prjrole))
    print('di_dirs = ')
    for x,y in di_dirs.items():
        print(x,y)
    print()
def fn_set_dir(i_dirname, i_dirvalue, i_mode='safe'):
    global st_prjname
    global st_prjrole
    global di_dirs
    fn_init()
    r='N'
    if i_mode == 'safe':
        r='Y'
        if di_dirs[i_dirname] == None:
            di_dirs[i_dirname] = i_dirvalue
            x='Value of Key:{} initialized to\n  {}'
            print(x.format(i_dirname,di_dirs[i_dirname]))
    if i_mode == 'force':
        r='Y'
        di_dirs[i_dirname] = i_dirvalue
        x='Value of Key:{} reset to\n  {}'
        print(x.format(i_dirname,di_dirs[i_dirname]))
    if r != 'Y':
        print('Valid modes are listed below:\n  safe  force')
        print('Default mode: safe')
