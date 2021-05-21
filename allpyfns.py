
# Start of this module

# Importing necessary packages
from   pathlib import Path
import pandas as pd

def fn_initvar(i_prjhome):
    global st_prjname
    global st_prjrole
    global po_prjhome
    st_prjname='prj2bzk'
    st_prjrole='dev'
    po_prjhome=Path(i_prjhome)    
# Defining functions in this module
def fn_init(i_prjhome):
# Initialize module
    print('Initializing AllPyfunctions module')
    fn_setup()
    fn_getsqlm('zzzz')
    print(st_sqlm, end='')
    fn_getsqlc('zzzz')
    print(st_sqlc, end='')
def fn_setup():
# Setup module
    global li_sqlm
    global df_sqlm
    global li_sqlc
    global df_sqlc
    fo_mt = po_prjhome / 'allsqmsg.sql'
    fo_mc = po_prjhome / 'allsqmsg.csv'
    fo_ct = po_prjhome / 'allsqcmd.sql'
    fo_cc = po_prjhome / 'allsqcmd.csv'
    with open(fo_mt, 'r') as f: li_sqlm = f.readlines()
    df_sqlm = pd.read_csv(fo_mc)
    df_sqlm['sql_id'] = df_sqlm['sql_id'].astype('string')
    with open(fo_ct, 'r') as f: li_sqlc = f.readlines()
    df_sqlc = pd.read_csv(fo_cc)
    df_sqlc['sql_id'] = df_sqlc['sql_id'].astype('string')
def fn_getsqlm(i_sqlid):
# Getting sql message text for the given sql-id
    global st_sqlm
    z=''
    for x in df_sqlm.index:
        if df_sqlm.iloc[x,0] == i_sqlid:
            for y in range(df_sqlm.iloc[x,1], df_sqlm.iloc[x,2]):
                z=z+li_sqlm[y]
    st_sqlm=z
def fn_getsqlc(i_sqlid):
# Getting sql command text for the given sql-id
    global st_sqlc
    z=''
    for x in df_sqlc.index:
        if df_sqlc.iloc[x,0] == i_sqlid:
            for y in range(df_sqlc.iloc[x,1], df_sqlc.iloc[x,2]):
                z=z+li_sqlc[y]
    st_sqlc=z

# End of this module

