import os
import numpy as np
import pandas as pd

"""
    This python module aims to read the data, convert it into a dataframe and provide the meta data like 
    data types, number of missing records and missing record percentage. It also help user to chnage the 
    data type
"""

def read_data(file, sep=None, na_values=None):
    """
        args: 
            file: file path means the path to dataset like C://user/xx/data.csv. It can be a csv or excel
            sep: In case of csv file the user can enter the separator like [comma, ;, space etc]
        output:
            df: A dataframe
    """
    ext = os.path.splitext(file)[1]
    csv = ['csv', 'tsv']
    xcel = ['xlsx', 'xlsb','xlsm']
    try:
        if ext in csv:
            df = pd.read_csv(file, sep=sep, na_values=na_values)
        if ext in xcel:
            df = pd.read_excel(file)
    except OSError as e:
        print("File not found")
        
    return df


def meta_data(df):
    """
        Args: 
            df: Dataframe
        output:
            meta_df : a dataframe which contains meta data of dataframe
    """
    meta_df = pd.DataFrame()
    meta_df['columns'] = df.columns
    meta_df.index = meta_df['columns']
    meta_df['dtypes'] = df.dtypes
    meta_df['num_null'] = df.isna().sum()
    meta_df['pct_null'] = df.isna().sum() * 100 / df.shape[0]
    
    meta_df = meta_df.drop('columns', axis=1)
    return meta_df

def modify_df(df, dtypes, remark=None):
    """
        The user can change the data types of various columns in the data frame.
        
        args:
            df: Dataframe
            dtypes: A dictionary which contains columns as key and data types as values. The 
            column data types will be changed as per value data types
        output:
            df: The dataframe with changed data types 
            meta_df: The changed meta_df
    """
    
    meta_df = meta_data(df)
    
    if type(dtypes) == 'dict':
        for i in df:
            df[i] = df[i].astype(dtypes[i])
    else:
        print("please provide the dtypes in dictionary format, where keys are column names")
        
    meta_df['changed_dtypes'] = df.dtypes
    
    return df, meta_df
