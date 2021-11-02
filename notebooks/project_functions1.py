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

"""
def sort(df):
    print("aaaa")
    return df
"""

def group_by_majorCat(df):
    
    major_cat_list = df['Major_category'].unique()
    cat_number = []
    for category in major_cat_list:
        cat_number.append( (df.Major_category == category).sum() )
    
    
    df1 = df.groupby('Major_category', as_index=False).sum()
    
    return df1