import pandas as pd
import joblib
import numpy as np
from utils.preprocessing import clean_select_data
from utils.preprocessing import encoding
import os
import platform

print('One moment, the model is calculating the predictions...')

linregr = joblib.load('models/lin_regres_houses.pkl')


clean_select_data('data/new_data.csv')
df = pd.read_csv('data/preprocessed_data.csv')
encoding_df = encoding(df)

log_prices = linregr.predict(encoding_df)
power_prices = np.power(10, log_prices)
#print("This is a list of the predictions the model made: ", final_prices)

rounded_prices = [round(price,2) for price in power_prices]
predictions = [round(price,-2) for price in rounded_prices]

#save into file:
predictions_df = pd.DataFrame(predictions, columns=['Predicted_Price'])
predictions_df.to_csv('predictions_new_data.csv', index=False)

#open csv-file when saved:
#check if Windows/Mac/Linux:
os_name = platform.system()
#check if exists:
if os.path.exists('predictions_new_data.csv'):
    if os_name == "Windows":
        os.system(f"start {'predictions_new_data.csv'}")
    elif os_name == "Linux":
        os.system(f"xdg-open {'predictions_new_data.csv'}")
    elif os_name == "Darwin":
        os.system(f"open {'predictions_new_data.csv'}")
    else:
        print("Operator not known")
else:
    print("Error: CSV-file is not know, try running the program again.")
print("The CSV-file with the predicted prices is now open.")