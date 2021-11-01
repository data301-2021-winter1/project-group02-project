#Project functions Alejandro Builes (notebook 2: analysis 2)
import pandas as pd 
import numpy as np 


def clean_data(data):
    is_null = data.isnull() 
    row_has_null = is_null.any(axis=1)
    rows_with_null = data[row_has_null]
    rows_with_null
    df = data.drop(['Major_code', 'Sample_size', 'College_jobs', 'Non_college_jobs'], axis = 1)
    cleandata = df.drop([21]) #Column with null values dropped 
    return cleandata

def group_data_by_major_category(data):
    df1 = data.groupby('Major_category', as_index=False).sum()
    df2 = df1.to_numpy()
    n = len(df2)
    for i in range(n):
        df2[i] = list(df2[i])
    for i in range(n):
        df2[i][11] = df2[i][10] / df2[i][2] # Unemployment_rate = Unemployed / Total
        df2[i][5] = df2[i][4] / df2[i][2] # ShareWomen = Women / Total
    
        df1 = pd.DataFrame(df2, columns = df1.columns)
    df1
    return df1
    
