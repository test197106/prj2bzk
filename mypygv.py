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
