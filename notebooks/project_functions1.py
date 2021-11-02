# Egor's functions for the project
import pandas as pd
import numpy as np

#Loads unprocessed data from the given path
def load_raw(path):
    df = pd.read_csv(path)
    return df

#Cleans the data, drops some columns and rows without values
def process_data(path):
    df = pd.read_csv(path)
    df = df.dropna()
    cleanData = df.drop(['Major_code', 'Sample_size', 'College_jobs', 'Non_college_jobs', 'Low_wage_jobs', 'Rank'], axis=1)
    return cleanData

def group_by_majorCat(df):
    """
    major_cat_list = df['Major_category'].unique()
    cat_number = []
    for category in major_cat_list:
        cat_number.append( (df.Major_category == category).sum() )
    """
    
    df1 = df.groupby('Major_category', as_index=False).sum()
    
    return df1

def fix_unempoyment_and_wshare(data):
    df2 = data.to_numpy()
    n = len(df2)
    for i in range(n):
        df2[i] = list(df2[i])
    for i in range(n):
        df2[i][11] = df2[i][9] / df2[i][1] # Unemployment_rate = Unemployed / Total
        df2[i][5] = df2[i][3] / df2[i][1] # ShareWomen = Women / Total
    ds = pd.DataFrame(df2, columns = data.columns)
    return ds