import pandas as pd
import numpy as np

def unprocessed(csv_file):
    df = pd.read_csv(csv_file)
    return df
    
def load_process(csv_file):
    df = pd.read_csv(csv_file)
    df1=(df.dropna(subset=["Total","Men","Women","ShareWomen"]) 
        .sort_values("Major_category")
        .reset_index(drop=True)
        )    
    return df1
    
def sort_majorcategory(dfp):
    df1 = dfp.groupby("Major_category", as_index=False).sum()
    df2 = pd.melt(df1, id_vars="Major_category", value_vars=["Part_time", "Full_time_year_round", "Employed", "Unemployed"],var_name ='JobType', value_name ='Number_employed')
    return df2
    
def majorcategory_mean(dfp):
    return dfp.groupby('Major_category', as_index=False).mean()