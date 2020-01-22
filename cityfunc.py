import pandas as pd
import os.path

def check_file(ifile):
    if os.path.isfile(ifile):
        return 0
    else:
        return 1
    
def check_columns(ifile):
    req_col_list=['name', 'group', 'year', 'value']
    df=pd.read_csv(ifile,nrows=2)
    file_col_list=df.columns
    check = all ( item in file_col_list for item in req_col_list)

    if check is True:
        return 0
    else:
        return 1
