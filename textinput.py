import csv
import os
import pandas as pd
import datetime as dt
df = pd.DataFrame(columns=['ID','By Market','Data','Last Updated','Status'])

def add_data(id,market,data,date,time,choice):
    if os.path.exists('data.csv') ==  False:
        
        cwd = os.getcwd()
        path = cwd + "/data.csv"

        df.to_csv(path)
    
    date_time = str(date.strftime("%d/%m/%Y")) + " " + str(time.strftime("%H:%M:%S"))
    df.loc[len(df)+1] = [id,market,data,date_time,choice]
    df.to_csv('data.csv', mode='r+')

def summarize():
    if os.path.exists('data.csv') ==  True:
        sum_df = pd.read_csv('data.csv')
    else:
        sum_df = df
        

    sum_df = pd.DataFrame(sum_df.groupby(['By Market','Status']).size())
    sum_df = sum_df.rename(columns={0:'Count'})
    return sum_df

def display():
    if os.path.exists('data.csv') ==  False:
        return pd.DataFrame(columns=['ID','By Market','Data','Last Updated','Status'])
    else:
        dis_df = pd.read_csv('data.csv')
        dis_df = dis_df[['ID','By Market','Data','Last Updated','Status']]
        return dis_df
        


# df1 = pd.DataFrame(df.groupby(['By Market','Status']).size().groupby(level=1).max())



