import pandas as pd
from utils.a_import_data import data_import
from sklearn.metrics import mean_squared_error



def clean_select__data():
    """
    Preprocess the data.

    Parameters:
    - df_raw: DataFrame containing the raw data.

    Returns:
    - df: DataFrame containing the preprocessed data.
    """
        
    df_raw = data_import()
    #selecting only the data for houses
    df = df_raw[df_raw['PropertySubType'] == 'HOUSE']
    #For the model I only want to work with the variable with the best correlation (Price-LivingArea-BedroomCount):
    df = df[['Price', 'LivingArea','Province','BedroomCount']]
    #removing the rows with empty Prices and LivingArea
    df.dropna(subset=['Price', 'LivingArea'], inplace=True)
    #removing index from df because otherwise it gives NaN-values becaus after cleaning, indexes are non exsistent
    df.reset_index(drop=True, inplace=True) 

    return df






    