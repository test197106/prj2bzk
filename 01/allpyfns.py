

import os
import sys
import platform
import sqlite3 as sq3
import pandas as pd
import numpy as np
from   pathlib import Path
from   datetime import datetime
import time
import pandas as pd
import datetime as dt
import shutil
import uuid
#import requests
#import json
#import re
import importlib
import mypygvar as gv


def fn_reload():
    x=importlib.reload(sys.modules['allpyfns'])
    y=str(x).replace('>','').replace("'","").split()[3]
    print('Reloaded functions from {}'.format(y))


def fn_cr_sq3exe(i_4lr, i_exefname, i_exefile):
    ft_now=datetime.now()
    li_f=['p1s0', 0, 0, 1, i_4lr, 'sq3ex', i_exefname, 0, 0.0, True, ft_now, i_exefile ]
    j=len(df_files.index)
    df_files.loc[j] = li_f


def fn_cr_sq3inp(i_4lr, i_p, i_s, no_e, no_t):
    ft_now=datetime.now()
    i_e = 'e' + str(no_e)
    fo_loc = po_wrkbase / i_p / i_s / i_e
    fo_loc.mkdir(mode=0o755, parents=True, exist_ok=True)
    fs_psn = i_p + i_s
    fs_en  = i_4lr
    fs_fn  = fs_en + '_' + str(no_t) + '.txt'
    fo_ff  = fo_loc / fs_fn
    li_f=[fs_psn, 0, no_e, no_t, fs_en, 'sq3in', fs_fn, 0, 0.0, True, ft_now, fo_ff ]
    j=len(df_files.index)
    df_files.loc[j] = li_f


def fn_cr_sq3out(i_4lr, i_p, i_s, no_e, no_t):
    ft_now=datetime.now()
    i_e = 'e' + str(no_e)
    fo_loc = po_wrkbase / i_p / i_s / i_e
    fo_loc.mkdir(mode=0o755, parents=True, exist_ok=True)
    fs_psn = i_p + i_s
    fs_en  = i_4lr
    fs_fn  = fs_en + '_' + str(no_t) + '.txt'
    fo_ff  = fo_loc / fs_fn
    li_f=[fs_psn, 0, no_e, no_t, fs_en, 'sq3ou', fs_fn, 0, 0.0, True, ft_now, fo_ff ]
    j=len(df_files.index)
    df_files.loc[j] = li_f


def fn_setup_sqlite3():
    # Find the executable path name for sqlite3 exec file
    fv_out=platform.system()
    if  fv_out == 'Windows':
        fs_exefname = 'sqlite3.exe'
    else:
        fs_exefname = 'sqlite3'
    fo_exefile=Path(shutil.which(fs_exefname)).resolve()
    fn_cr_sq3exe('exe0',fs_exefname,fo_exefile)
    print(fo_exefile)
    fn_cr_sq3inp('inp0', 'p1', 's0', 0, 1)
    fn_cr_sq3out('out0', 'p1', 's0', 0, 1)


def fn_create_di_dbs():
    global di_dbs
    di_dbs = {}
    for x in df_files.index:
        if df_files.loc[x,'e_type'] == 'sq3db':
            y=df_files.loc[x,'e_name']
            z=str(df_files.loc[x,'f_file'])
            di_dbs.update({y:z})
    for k in di_dbs:
        p = k + ' : ' + di_dbs.get(k)
        print(p)
    print('di_dbs recreated')


def fn_create_sq3dbf(i_3lr, i_p, i_s):
    global di_dbs
    ft_now=datetime.now()
    fo_loc = po_wrkbase / i_p / i_s / 'e0'
    fo_loc.mkdir(mode=0o755, parents=True, exist_ok=True)
    fs_psn = i_p + i_s
    fs_fn  = i_3lr + '_1_sq3.dbf'
    fo_ff  = fo_loc / fs_fn
    li_f=[fs_psn, 0, 0, 1, i_3lr, 'sq3db', fs_fn, 0, 0.0, True, ft_now, fo_ff ]
    j=len(df_files.index)
    df_files.loc[j] = li_f
    with open(fo_ff, 'w') as f:
        pass
    print('Updating dictionary')
    fn_create_di_dbs()


# Checkpoint important information that might be needed after a cold restart
def do_ckpt_type_a():
    global df_files
    global df_events    
    fv_uuid=str(uuid.uuid4()).replace('-', '')
    
    # Saving df_files
    po_hsd_df_files  = po_hisbase / 'saved' / 'df_files'
    po_hsd_df_files.mkdir(mode=0o755, parents=True, exist_ok=True)
    po_his_df_files  = po_hsd_df_files / fv_uuid
    try:
        shutil.copyfile(po_fls_scv, po_his_df_files)
        print('\nCopying {}\n     to {}'.format(po_fls_scv,po_his_df_files))
    except:
        pass
    
    # Saving df_events
    po_hsd_df_events = po_hisbase / 'saved' / 'df_events'
    po_hsd_df_events.mkdir(mode=0o755, parents=True, exist_ok=True)
    po_his_df_events = po_hsd_df_events / fv_uuid
    try:
        shutil.copyfile(po_eve_scv, po_his_df_events)
        print('\nCopying {}\n     to {}'.format(po_eve_scv,po_his_df_events))
    except:
        pass


# Create df_events dataframe for stroring time records of events in this project
def fn_it_df_events():
    global df_events
    df_events = pd.DataFrame(columns=cf_events)
def fn_cc_df_events():
    df_events['fn_name'  ] = df_events['fn_name'  ].astype('string')
    df_events['b_time'   ] = df_events['b_time'   ].astype('datetime64[ns]')
    df_events['b_remarks'] = df_events['b_remarks'].astype('string')
    df_events['e_time'   ] = df_events['e_time'   ].astype('datetime64[ns]')
    df_events['e_remarks'] = df_events['e_remarks'].astype('string')
    #df_events['ela_secs' ] = df_events['ela_secs' ].astype(datetime.timedelta)
    df_events['status'   ] = df_events['status'   ].astype('int')
def fn_log_event(i_fn, i_fn_det, i_bt, i_et, i_msg, i_rc):
    j=len(df_events.index)
    f_ela=i_et-i_bt
    df_events.loc[j] = [i_fn, i_bt, i_fn_det, i_et, i_msg, f_ela, i_rc ]
    df_events.to_csv(po_eve_scv, header=True, index=False)
    print('{} {} in {} seconds'.format(df_events.loc[j,'status'],df_events.loc[j,'e_remarks'],
                            df_events.loc[j,'ela_secs']))


def fn_cr_df_events():
    #fn_it_df_events()
    global df_events
    st_col='fn_name,b_time,b_remarks,e_time,e_remarks,ela_secs,status\n'
    if not po_eve_scv.exists():
        print("Creating a blank events.csv file")
        with open(po_eve_scv, 'a') as g:
            g.write(st_col)
    df_events = pd.read_csv(po_eve_scv)
    fn_cc_df_events()
    print(df_events.info())
    #print(df_events)


def fn_restart_df_files():
    global df_files
    global cf_files_r
    fv_inpfile=Path(po_fls_bkp)
    df_files = pd.read_csv(fv_inpfile)
    fn_cc_df_files() 
    print(df_files.info())
    print('\nShowing normal columns:\n')
    print(df_files[ cf_files_r ])
    print('\n\nShowing LONG columns:\n')   
    for i in df_files.index:
        print( str(df_files.iloc[i,1]) + ' ' + str(df_files.iloc[i,11]) )


def fn_load_df_files(i_inpfile):
    global df_files
    global cf_files_r
    fv_inpfile=Path(i_inpfile)
    df_files = pd.read_csv(fv_inpfile)
    fn_cc_df_files()
    print(df_files.info())
    print('\nShowing normal columns:\n')
    print(df_files[ cf_files_r ])
    print('\n\nShowing LONG columns:\n')   
    for i in df_files.index:
        print( str(df_files.iloc[i,1]) + ' ' + str(df_files.iloc[i,11]) )


# Create df_files dataframe for stroring metadata about files processed
def fn_it_df_files():
    global df_files
    global cf_files
    global cf_files_r
    df_files = pd.DataFrame(columns=cf_files)


def fn_cc_df_files():
    df_files['ps_name'] = df_files['ps_name'].astype('string')
    df_files['f_id'] = df_files['f_id'].astype('int')
    df_files['e_id'] = df_files['e_id'].astype('int')
    df_files['t_id'] = df_files['t_id'].astype('int')
    df_files['e_name'] = df_files['e_name'].astype('string')
    df_files['e_type'] = df_files['e_type'].astype('string')
    df_files['f_name'] = df_files['f_name'].astype('string')
    df_files['f_size'] = df_files['f_size'].astype('int')
    df_files['s_pct'] = df_files['s_pct'].astype('float')
    df_files['isValid'] = df_files['isValid'].astype('bool')
    df_files['f_modified'] = df_files['f_modified'].astype('datetime64[ns]')


def fn_show_df_files(i_ps_name):
    df_files.to_csv(po_fls_scv, header=True, index=False)
    df_files.to_csv(po_fls_bkp, header=True, index=False)
    tdf_temp1=df_files.iloc[np.where(df_files.ps_name == i_ps_name)]
    print(df_files.info())
    print('\nShowing normal columns:\n')
    print(tdf_temp1[ cf_files_r ])
    print('\n\nShowing LONG columns:\n')   
    for i in tdf_temp1.index:
        print( str(df_files.iloc[i,1]) + ' ' + str(df_files.iloc[i,11]) )


def fn_cr_df_files():
    if po_fls_scv.exists():
        fv_uuid=str(uuid.uuid4()).replace('-', '')
        po_fls_saved = po_hisbase / 'saved' / 'df_files'
        po_fls_saved.mkdir(mode=0o755, parents=True, exist_ok=True)
        po_fls_sav = po_fls_saved / fv_uuid
        po_fls_scv.rename(po_fls_sav)
        print("Renaming files.csv to saved/df_files/{0}".format(fv_uuid))
    fn_it_df_files()
    fn_cc_df_files()
    print(df_files.info())
    print(df_files)


def fn_closing_event(i_ps, i_inc_di_dbs='Y'):
    global df_files
    global di_dbs
    global cf_files
    fn_cc_df_files()
    fn_cc_df_events()
    fn_show_df_files(i_ps)
    fn_imptbl_info(i_inc_di_dbs)
    do_ckpt_type_a()
    df_files = pd.DataFrame(columns=cf_files)
    di_dbs={}
    print(df_files)
    print(di_dbs)


def fn_imptbl_info(i_inc_di_dbs='Y'):
    print(df_files.info())
    print(df_events.info())
    fs_a=len(df_files.index)
    fs_b=len(df_events.index)
    print('\ndf_files count : {}\ndf_events count: {}'.format(fs_a,fs_b))
    if i_inc_di_dbs == 'Y':
        print('Contents of di_dbs')
        print(di_dbs)


def fn_p1s0_tasks():
    # Predefined Variables. Please do not edit the values in this cell
    f_btime_o=datetime.now()

    global cf_events
    global df_events
    global cf_files
    global cf_files_r
    global df_files
    global st_prog_start_dir
    global st_sq3exe
    global po_wrkbase
    global li_101_crdir_fmwb
    global li_102_cdwb_linkstt
    global po_eve_scv
    global po_fls_scv
    global po_fls_bkp
    global po_zipfile
    global po_hisbase
    global po_sq3exe
    global di_dbs

    # Saving the current directory path when program launched
    st_prog_start_dir=str(Path.cwd())
    print(st_prog_start_dir)

    # Set workbase directory
    si_zipfile=gv.di_u['st_zipfile_1']
    po_zipfile = Path(si_zipfile)
    d=gv.di_u['st_data_top_1']
    po_wrkbase = Path(d)
    print(po_wrkbase)
    po_hisbase = Path(d)/'his'
    print(po_hisbase)
    
    # Entries for creating directories in wb
    li_101_crdir_fmwb = [
      ['p1', 's0', 'e0']
    , ['p2', 's0', 'e0']
    , ['p3', 's0', 'e0']
    , ['p4', 's0', 'e0']
    , ['p5', 's0', 'e0']
    , ['p6', 's0', 'e0']
    , ['p7', 's0', 'e0']
    ]

    # Entries for creating sym inks in wb
    li_102_cdwb_linkstt = [
      ['p1.BDI', 'p1' ]  
    , ['p2.ETL', 'p2' ]
    , ['p3.EDA', 'p3' ]
    , ['p4.MDO', 'p4' ]
    , ['p5.MCU', 'p5' ]
    , ['p6.MPL', 'p6' ]
    , ['p7.RQI', 'p7' ]
    ]

    for x in li_101_crdir_fmwb:
        Path(po_wrkbase / x[0] / x[1] / x[2]).mkdir(mode=0o755, parents=True, exist_ok=True)

    os.chdir(po_wrkbase)
    print(Path.cwd())
    for x in li_102_cdwb_linkstt:
        try:
            t_a=Path(x[0])
            t_b=Path(x[1])
            t_a.symlink_to(t_b, target_is_directory=True)
        except:
            continue
    os.chdir(st_prog_start_dir)
    print(Path.cwd())

    po_eve_scv = po_wrkbase / 'p1' / 's0' / 'e0' / 'events.csv'
    print(po_eve_scv)

    po_fls_scv = po_wrkbase / 'p1' / 's0' / 'e0' / 'files.csv'
    print(po_fls_scv)

    po_fls_bkp = po_wrkbase / 'p1' / 's0' / 'e0' / 'files.csv.bkp'
    print(po_fls_bkp)

    # Define column names of df_files
    cf_files = ['ps_name', 'f_id', 'e_id', 't_id', 'e_name', 'e_type', 
                'f_name', 'f_size', 's_pct', 'isValid', 'f_modified', 'f_file' ]

    cf_files_r = ['ps_name', 'f_id', 'e_id', 't_id', 'e_name', 'e_type', 
                  'f_name', 'f_size', 's_pct', 'isValid', 'f_modified' ]
    
    cf_events = [ 'fn_name', 'b_time', 'b_remarks', 'e_time', 'e_remarks', 'ela_secs', 'status' ]

    # Create dataframes for events
    fn_cr_df_events()

    # Create dataframes for file-metadata
    fn_cr_df_files()

    # Phase closing tasks
    f_etime_o=datetime.now()
    fn_log_event('fn_setupGround', '', f_btime_o, f_etime_o, 'Setup ground for pipes, end points', 0)


def fn_install_p1s1e():
    global p1_s1_e0
    global li_103_p1_s1_e0
    # Entries for creating directories in wb
    li_201_crdir_fmwb = [
      ['p1', 's1', 'e0']
    ]

    for x in li_201_crdir_fmwb:
        Path(po_wrkbase / x[0] / x[1] / x[2]).mkdir(mode=0o755, parents=True, exist_ok=True)

    # Set the unzip location for extracting the contents of zipfile
    p1_s1_e0 = po_wrkbase / 'p1' / 's1' / 'e0'
    print(p1_s1_e0)

    # Provide meta data about input files
    li_103_p1_s1_e0 = [
      ['train_data.csv',          'outage_dna',  'csv' ]
    , ['student_test.csv',        'outage_dnb',  'csv' ]
    , ['broadband_data.csv',      't_bband',     'csv' ]
    , ['outage_data.csv',         't_outage',    'csv' ]
    , ['report_data.csv',         't_report',    'csv' ]
    , ['server_data.csv',         't_server',    'csv' ]
    ]


def fn_rcvdata_p1s1e():
    f_btime=datetime.now()
    shutil.unpack_archive(po_zipfile, p1_s1_e0)
    f_etime=datetime.now()
    fn_log_event('fn_rcvdata_p1s1e', '', f_btime, f_etime, 'Received data in P1S1E', 0)


def fn_chktank_p1s1e(i_inplist):
    print('I am in fn_chktank_p1s1e')
    w_c=datetime.now()
    j=len(df_files.index)
    f_id=0
    e_id=0
    for x in i_inplist:
        e_id=e_id+1
        st_t1=[]
        for y in p1_s1_e0.rglob(x[0]):
            st_t1.append(str(y))
        t_id=0
        for z in sorted(st_t1):
            z_p=Path(z)
            t_id=t_id+1
            f_id=f_id+1
            li_t1=['p1s1', f_id, e_id, t_id, x[1], x[2], z_p.name,
                   z_p.stat().st_size, 0, True, w_c, z_p.resolve()]
            df_files.loc[j] = li_t1
            j=j+1
    fn_cc_df_files()
    fn_show_df_files('p1s1')
    print('I am out fn_chktank_p1s1e')


def fn_p1s1_tasks():
    print('I am in fn_p1s1_tasks')
    f_btime_o=datetime.now()
    
    # Create pipe p1s1 for receiving data
    fn_install_p1s1e()
    
    # Receive data from Input_Zipfile to P1S1E
    fn_rcvdata_p1s1e()

    # Check details of the data received
    fn_chktank_p1s1e(li_103_p1_s1_e0)

    # Phase closing tasks
    f_etime_o=datetime.now()
    fn_log_event('fn_irc_p1s1e', '', f_btime_o, f_etime_o, 'Install, Receive and Check P1S1E', 0)
    fn_closing_event('p1s1','N')
    print('I am out fn_p1s1_tasks')


def fn_copy_df_files(i_src_pname, i_src_sname, i_tgt_pname, i_tgt_sname):
    i_src_psname = i_src_pname + i_src_sname
    i_tgt_psname = i_tgt_pname + i_tgt_sname
    j=len(df_files.index)
    tdf_temp1=df_files.iloc[np.where(df_files.ps_name == i_src_psname)]
    for i in tdf_temp1.index: 
        li_t1=df_files.loc[i].to_list()
        li_t1[0]=i_tgt_psname
        tgt_c2 = 'e' + str(li_t1[2])
        tgt_fname = str(li_t1[3]) + '.' + li_t1[4] + '.csv'
        li_t1[6] = tgt_fname
        li_t1[11] = po_wrkbase / i_tgt_pname / i_tgt_sname / tgt_c2 / tgt_fname
        df_files.loc[j] = li_t1
        j=j+1
    fn_cc_df_files()
    fn_show_df_files(i_tgt_psname)


def fn_install_p1s2e():
    # Entries for creating directories in wb
    li_301_crdir_fmwb = [
      ['p1', 's2', 'e1']
    , ['p1', 's2', 'e2']
    , ['p1', 's2', 'e3']
    , ['p1', 's2', 'e4']
    , ['p1', 's2', 'e5']
    , ['p1', 's2', 'e6']
    , ['p1', 's2', 'e7']
    ]

    for x in li_301_crdir_fmwb:
        Path(po_wrkbase / x[0] / x[1] / x[2]).mkdir(mode=0o755, parents=True, exist_ok=True)

    # Layout P1S2 pipes
    fn_copy_df_files('p1', 's1', 'p1', 's2')


def fn_rcvdata_p1s2e():
    df1 = df_files.iloc[np.where(df_files.ps_name == 'p1s1')]
    df2 = df_files.iloc[np.where(df_files.ps_name == 'p1s2')]
    df3 = pd.merge(df1, df2, on='f_id', how='inner')
    df4=df3.iloc[:, [1,2,5,6,17,11,22]]
    df5a = df4.iloc[np.where(df4.e_type_x == 'csv')]
    df5b = df4.iloc[np.where(df4.e_type_x == 'txt')]

    for x in df5a.index:
        s_f=df5a.loc[x][5]
        t_f=df5a.loc[x][6]
        fv_src = Path(s_f)
        fv_tgt = Path(t_f)

        fv_src.rename(fv_tgt)
        print('\nMoving {}\n    to {}'.format(s_f,t_f))
        
    for x in df5b.index:
        s_f=df5b.loc[x][5]
        t_f=df5b.loc[x][6]
        fv_src = Path(s_f)
        fv_tgt = Path(t_f)
        
        sf = open(fv_src, 'r')
        tf = open(fv_tgt, 'w')
        Lines = sf.readlines()
        for line in Lines:
            new_line=line.replace('|',',')
            tf.writelines(new_line)
        sf.close()
        tf.close()
        
        print('\nModify {}\n    to {}'.format(s_f,t_f))


def fn_chktank_p1s2e():
    for x in df_files.index:
        v_1=df_files.iloc[x][0]
        v_2=df_files.iloc[x][5]
        if (( v_1 == 'p1s2') and (v_2 == 'txt')):
            print('\nFollowing entry')
            print(df_files.iloc[x])
            print('\nchanged to')
            df_files.iloc[x,5]='csv'
            print(df_files.iloc[x])
    fn_show_df_files('p1s2')


def fn_p1s2_tasks():
    # Opening tasks for this phase
    f_btime_o=datetime.now()
    fn_restart_df_files()
    fn_show_df_files('p1s1')  

    # Create pipe p1s2 for receiving data
    fn_install_p1s2e()
    
    # Receive data from P1S1E to P1S2E
    fn_rcvdata_p1s2e()

    # Check details of the data received
    fn_chktank_p1s2e()

    # Closing tasks for this phase
    f_etime_o=datetime.now()
    fn_log_event('fn_irc_p1s2e', '', f_btime_o, f_etime_o, 'Install, Receive and Check P1S2E', 0)
    fn_closing_event('p1s2','N')


def fn_install_p1s3e():
    fn_setup_sqlite3()
    
    # Create information repository for this project
    fn_create_sq3dbf('zz1', 'p1', 's0')
    fn_cc_df_files()
    fn_cc_df_events()
    fn_show_df_files('p1s0')
    
    # Creae the database for this phase
    fn_create_sq3dbf('db0', 'p1', 's3')
    fn_cc_df_files()
    fn_cc_df_events()
    fn_show_df_files('p1s3')


def fn_rcvdata_p1s3e(i_sqlid):
    f_btime_o=datetime.now()

    for x in df_files.iloc[np.where((df_files.e_type=='sq3ex')&(df_files.e_name=='exe0'))].loc[:,'f_file']:
        ff_exe=str(x)
    for x in df_files.iloc[np.where((df_files.e_type=='sq3in')&(df_files.e_name=='inp0') 
                                    & (df_files.t_id==1))].loc[:,'f_file']:
        ff_inp=str(x)
    for x in df_files.iloc[np.where((df_files.e_type=='sq3ou')&(df_files.e_name=='out0') 
                                    & (df_files.t_id==1))].loc[:,'f_file']:
        ff_out=str(x)
    f_run = '"' + ff_exe + '" < "' + ff_inp + '"' + ' > "' + ff_out + '"'

    get_sqlstr(i_sqlid)
   
    fli_1=df_files.loc[np.where(df_files.ps_name=='p1s2')
                        ].loc[:,['e_name', 't_id', 'f_file' ]].values.tolist()

    for x in fli_1:
        fe_nm, ft_id, ff_fl = x
        mesg='\nImporting {sv_01}\n       to TABLE {sv_02}_{sv_03:02}'
        mesg2=mesg.format(sv_01=ff_fl,sv_02=fe_nm,sv_03=ft_id)
        z=st_opval.format(k=di_dbs,sv_01=ff_fl,sv_02=fe_nm,sv_03=ft_id)
        #print(z)
        f_ta='p1s3:{sv_02}_{sv_03:02}:Import'
        f_tb=f_ta.format(sv_01=ff_fl,sv_02=fe_nm,sv_03=ft_id)
        #print(f_tb)
        with open(ff_inp, "w") as f:
            f.write(z)
        print(mesg2)
        fi_btime=datetime.now()
        f_rc = os.system(f_run)
        fi_etime=datetime.now()
        #print(f_rc)
        #with open(ff_out, 'r') as f:
        #    print(f.read())
        fn_log_event('fn_execsql', 'Importing table', fi_btime, fi_etime, f_tb, f_rc)
    fn_cc_df_files()
    fn_cc_df_events()
    fn_show_df_files('p1s3')
    f_etime_o=datetime.now()
    fn_log_event('fn_rcvdata_p1s3e', '', f_btime_o, f_etime_o, 'Received data in P1S3E', 0)


def fn_chktank_p1s3e(i_sqlid_a,i_sqlid_b,i_sqlid_c):
    f_btime_o=datetime.now()
    for x in df_files.iloc[np.where((df_files.e_type=='sq3ex')&(df_files.e_name=='exe0'))].loc[:,'f_file']:
        ff_exe=str(x)
    for x in df_files.iloc[np.where((df_files.e_type=='sq3in')&(df_files.e_name=='inp0') 
                                    & (df_files.t_id==1))].loc[:,'f_file']:
        ff_inp=str(x)
    for x in df_files.iloc[np.where((df_files.e_type=='sq3ou')&(df_files.e_name=='out0') 
                                    & (df_files.t_id==1))].loc[:,'f_file']:
        ff_out=str(x)
    f_run = '"' + ff_exe + '" < "' + ff_inp + '"' + ' > "' + ff_out + '" 2>&1'
    get_sqlstr(i_sqlid_a)
    print('\nCounting rows of all imported tables in P1S3')
    #print('\nExecuting following sql on P1S3')
    #print(st_opval)
    z=st_opval.format(k=di_dbs)
    #print(z)
    with open(ff_inp, "w") as f:
        f.write(z)
    fi_btime=datetime.now()
    f_rc = os.system(f_run)
    fi_etime=datetime.now()
    f_tb = 'SQL:' + str(i_sqlid_a)
    fn_log_event('fn_execsql', '', fi_btime, fi_etime, f_tb, f_rc)
    with open(ff_out, 'r') as f:
        print(f.read())
    
    get_sqlstr(i_sqlid_b)

    fli_1=df_files.loc[np.where(df_files.ps_name=='p1s2')
                        ].loc[:,['e_name', 't_id', 'f_file' ]].values.tolist()
    for x in fli_1:
        fe_nm, ft_id, ff_fl = x
        mesg='\nExecuting sql template on {sv_02}_{sv_03:02} table'
        mesg2=mesg.format(sv_01=ff_fl,sv_02=fe_nm,sv_03=ft_id)
        z=st_opval.format(k=di_dbs,sv_01=ff_fl,sv_02=fe_nm,sv_03=ft_id)
        #print(z)
        f_ta='p1s3:{sv_02}_{sv_03:02}:RowCount'
        f_tb=f_ta.format(sv_01=ff_fl,sv_02=fe_nm,sv_03=ft_id)
        #print(f_tb)
        with open(ff_inp, "w") as f:
            f.write(z)
        print(mesg2)
        fi_btime=datetime.now()
        f_rc = os.system(f_run)
        fi_etime=datetime.now()
        #print(f_rc)
        fn_log_event('fn_execsql', 'Counting rows', fi_btime, fi_etime, f_tb, f_rc)        
    get_sqlstr(i_sqlid_c)
    z=st_opval.format(k=di_dbs)
    with open(ff_inp, "w") as f:
        f.write(z)
    fi_btime=datetime.now()
    f_rc = os.system(f_run)
    fi_etime=datetime.now()
    f_tb = 'SQL:' + str(i_sqlid_c)
    fn_log_event('fn_execsql', '', fi_btime, fi_etime, f_tb, f_rc)
    with open(ff_out, 'r') as f:
        print(f.read())

    fn_cc_df_files()
    fn_cc_df_events()
    fn_show_df_files('p1s3')
    f_etime_o=datetime.now()
    fn_log_event('fn_chktank_p1s3e', '', f_btime_o, f_etime_o, 'Checked data in P1S3E', 0)
    do_ckpt_type_a()


def fn_p1s3_tasks():
    # Opening tasks for this phase
    f_btime_o=datetime.now()
    fn_restart_df_files()
    fn_show_df_files('p1s2')  
    fn_create_di_dbs()
    
    # Create pipe p1s3 for receiving data
    fn_install_p1s3e()
    
    # Receive data from P1S2E to P1S3E
    fn_rcvdata_p1s3e(122)

    # Check details of the data received
    fn_chktank_p1s3e(131,132,133)
        
    # Closing tasks for this phase
    f_etime_o=datetime.now()
    fn_log_event('fn_irc_p1s3e', '', f_btime_o, f_etime_o, 'Install, Receive and Check P1S3E', 0)
    fn_closing_event('p1s3')

