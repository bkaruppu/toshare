import pandas as pd
from cityfunc import *
import sys
import matplotlib.pyplot as plt

ifile="citydata.txt"
ofile="output.csv"



if check_file(ifile) == 0:
    if check_columns(ifile) == 0:
        df = pd.read_csv(ifile,usecols=['name', 'group', 'year', 'value'])
        current_year = 2017
        df1 = (df[df['year'].eq(current_year)]
            .sort_values(by='value', ascending=True)
            .head(5))
        df1.to_csv(ofile, sep=',', index=False)

        fig, ax = plt.subplots(figsize=(15, 8))
        ax.barh(df1['name'], df1['value'])
    else:
         print("Required columns do not Exist in Data File")
else:
    print("Data File does not Exist")
 
