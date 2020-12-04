from sklearn.preprocessing import StandardScaler, Normalizer, MinMaxScaler, OneHotEncoder
import pandas as pd

"""
This module aims to help in feature scaling and categorical feature encoding
"""

def scale(df, method='standard-scaler'):
    
    """
    Scale the databy scaling techniques default is standard scaler standard scaler
    
    Args:
        df: DataFrame
        method: Scaling methods can be choosen from minmax scaler, standard scaler and normalizer
    Returns:
        df: A dataframe with scaling technique applied
    """
    df2 = df.copy()
    if method == 'standard-scaler':
        sc = StandardScaler()
        df2 = sc.fit_transform(df2)
    
    elif method == 'minmax':
        msc = MinMaxScaler()
        df2 = msc.fit_transform()
        
    elif method == 'normalizer':
        norm = Normalizer()
        df2 = norm.fit_transform(df2)
        
    return df2

def encode(df, col_meth=None):
    
    """
        Encode categorical columns
        Args:
            df : The base dataframe
            col_meth: A dictionary which contains a column name as a key and encoding technique as value.
        Returns:
            df: An encoded dataframe
    """
    
    if col_meth:
        pass
    else:
        ohe = OneHotEncoder(drop_first=True)
        oc = ohe.fit_transform(df[['ocean_proximity']])
        columns = ohe.categories_.remove(ohe.drop_idx_[0])
        oc_df = pd.DataFrame(oc, columns=columns)
        df2 = pd.concat([df, oc_df], axis=1)
        df2.drop('ocean_proximity', axis=1, inplace=True)
        
    return df2