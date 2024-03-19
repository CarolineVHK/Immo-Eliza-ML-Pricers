import pandas as pd
from .import_data import data_import


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
    df = df[['Price', 'LivingArea','Province','BedroomCount','PropertySubType']]
    #removing the rows with empty Prices and LivingArea
    df.dropna(subset=['Price', 'LivingArea'], inplace=True)
    #removing index from df because otherwise it gives NaN-values becaus after cleaning, indexes are non exsistent
    df.reset_index(drop=True, inplace=True) 

    #saving the new dataFrame:
    #path for the CSV file
    output_file_path = "./data/preprocessed_data.csv"
    # Save df to CSV file
    df.to_csv(output_file_path, index=False)

    return df

    






    