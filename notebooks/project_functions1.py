# Egor's functions for the project

import pandas as pd
import numpy as np

def load_raw(path):
    #Loads unprocessed data from the given path
    
    df = pd.read_csv(path)
    return df

def process_data(path):
    #Cleans the data, drops some columns and rows without values
    
    df = pd.read_csv(path)
    df = df.dropna()
    cleanData = df.drop(['Major_code', 'Sample_size', 'Full_time', 'Part_time', 'Full_time_year_round', 'Rank', 'ShareWomen'], axis=1)
    return cleanData

def group_by_majorCat(df):
    #Groups dataset by major categories
    
    major_cat_list = df['Major_category'].unique()
    major_cat_list = np.sort(major_cat_list)   #Sorts the list alphabetically
    
    program_num_list = number_of_programs(major_cat_list, df)   #Returns a list with program numbers by major categories
    
    df1 = df.groupby('Major_category', as_index=False).sum()
    df1['Amount_of_Programs'] = program_num_list
    return df1

def fix_unempoyment(data):
    #Creates new column with correct unempoyment rate, drops the old one
    
    data['Correct_Unemployment_Rate'] = ( data['Unemployed'] / data['Total'] )
    ds = data.drop(['Unemployment_rate'], axis=1)
    return ds

def number_of_programs(mcat_list, data):
    #Returns a list with number of programs offered in each major category, helper function
    
    count = 0
    program_num = []
    for i in range( len(mcat_list) ):   #Cycles through the majors and records categories 
        for k in data['Major_category']:
            if mcat_list[i] == k:
                count += 1
        program_num.append(count)
        count = 0
    
    return program_num