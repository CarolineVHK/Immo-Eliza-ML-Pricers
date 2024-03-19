from utils_copy.import_data import data_import
from utils_copy.preprocessing import clean_select_data
from utils_copy.train import train_model
from utils_copy.model_LR import model_LR
from utils_copy.predict import predictions


def main():
    print('One moment, the model is calculating the predictions...')
    #import data
    data_import()
    #preprocessing the data (selection for only Houses, cleaning the data, handling missing values,...)
    clean_select_data(df_raw)
    #train the model
    train_model()
    #model used:
    model_LR()
    #predictions:
    predictions()

main()



