import os
import pandas as pd


def file_add_data(file,id,market,data,date_time,status):
    print(file)
    file_df = pd.read_csv(file)
    print(file_df)
    if os.path.exists('data.csv') ==  False:
        cwd = os.getcwd()
        path = cwd + "/data.csv"
        file_df.to_csv(path,mode='r+')
    else:
        cwd = os.getcwd()
        path = cwd + "/data.csv"
        df = pd.read_csv('data.csv')
        file_df = file_df[[id,market,data,date_time,status]]
        result = pd.concat([df,file_df])
        result.to_csv(path,mode='r+')