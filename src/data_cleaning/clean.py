import numpy as np
import pandas as pd

"""
    This module helps the user in cleaning data like handling bad values and filling null values
"""

def get_range(df):
    pass


def get_set(df):
    pass


def range_constraints(df, range_dict, except_dict):
    """
        Numerical values should be checked with invalid values and range constraints. The bad values will be
        set as null values.
        
        args:
            df: DataFrame
            range_dict: range constraints for numerical values like => {col: (1, 100)}
                        remember the min and max values will be compared with < and >. So value will be set as 
                        1 < val < 100
            except_dict: The values which shouldn't present in the columns like in area of the house column
                         0 is an unacceptable value. So those are set to None.
        returns:
            df: the modified dataframe
    """
    
    for i in df:
        df.loc[(df[i]<range_dict[i][0])|(df[i]>range_dict[i][0]), i] = np.nan
        df.loc[df[i]==except_dict[i], i] = np.nan
        
    return df

def set_constraints(df, set_dict):
    
    """
        Get the values which are not in the set for the columns and set the value to 0. Like states of India 
        is a set, if a state name 'abc' is there this function set that value to null
        
        args:
            df: DataFrame
            set_dict: A column name wise dictionary, like for vowel colum {vow:[a,e,i,o,u]}
        returns:
            df: The dataframe with modification
    """
    for i in df:
        