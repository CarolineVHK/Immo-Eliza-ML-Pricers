import pandas as pd
import numpy as np
from .import_data import data_import
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder


def clean_select_data(file_path):
    """
    Preprocess the data.

    Parameters:
    - df_raw: DataFrame containing the raw data.

    Returns:
    - df: DataFrame containing the preprocessed data.
    """
        
    df_raw = data_import(file_path)
    #selecting only the data for houses
    df = df_raw[df_raw['PropertySubType'] == 'HOUSE']
    #For the model I only want to work with the variable with the best correlation (Price-LivingArea-BedroomCount):
    df = df[['Price', 'LivingArea','Province','BedroomCount','PropertySubType']]
    #removing the rows with empty Prices and LivingArea
    df.dropna(subset=['Price', 'LivingArea'], inplace=True)
    #removing index from df because otherwise it gives NaN-values becaus after cleaning, indexes are non exsistent
    df.reset_index(drop=True, inplace=True) 
    #log10 from np on price: reduce effect from outliers
    df['Price'] = np.log10(df['Price'])

    #saving the new dataFrame:
    #path for the CSV file
    output_file_path = "./data/preprocessed_data.csv"
    # Save df to CSV file
    df.to_csv(output_file_path, index=False)

    return df

def encoding(new_data):
    df = clean_select_data('./data/raw_data.csv')
    #split the data
    #1. defining X (without the target-variable) and y (=target-value):
    X = df.drop(columns=['Price','PropertySubType'], axis=1)
    y = df['Price']
    #2. create the training and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  #training with 20% of the dataset

    #dealing with categorical data for'Province': turn categories into numbers:
    one_hot = OneHotEncoder(handle_unknown = "ignore", sparse_output=False)
    transformed_X_train = one_hot.fit_transform(X_train[['Province']])

    transformed_X_new_data = one_hot.transform(new_data[['Province']])
    transformed_X_new_data = pd.DataFrame(transformed_X_new_data, columns=one_hot.get_feature_names_out(['Province']))
    #add transfromed_X_df to the original df
    df_conc_new_data = pd.concat([new_data.reset_index(), transformed_X_new_data], axis=1).drop(["Province","Price","PropertySubType"], axis=1)

    return df_conc_new_data




    