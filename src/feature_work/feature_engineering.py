import numpy as np
import pandas as pd

"""
This module aims to create various features as wished by the user
"""

def binarize(df, cols=None, col_dict=None):
    
    """
    Binarize the continuous features. The default number of bins are 10 and default cols are all numeric 
    columns.
    
    Args:
        df : A data frame.
        cols: A dict which contains key as column names and values as number of bins
    returns:
        df: Dataframe with added columns
    """
    for i in df:
        if df[i].dtype == 'int':
            mod_col = str(i)+"_bin"
            df[mod_col] = pd.cut(df[i], bins=bins)
    return df