from utils.model_for_linear_regression import model_LR
from utils.preprocessing import clean_select_data
import pandas as pd
import numpy as np
import os
import platform

print('One moment, the model is calculating the predictions...')

#launching the model:
log_prices = model_LR() #---> this is an array, need to change
power_prices = np.power(10, log_prices)
#print("This is a list of the predictions the model made: ", final_prices)

rounded_prices = [round(price,2) for price in power_prices]
final_prices = [round(price,-2) for price in rounded_prices]
# print("This is a list of the predictions the model made: ", final_prices)

#path for csv
data_with_predictions = "./data/prediction_data.csv"
#save the df predicted_prices to CSV file
pd.DataFrame(final_prices, columns=['Predicted_Price']).to_csv(data_with_predictions, index=False)

#open csv-file when saved:
#check if Windows/Mac/Linux:
os_name = platform.system()
#check if exists:
if os.path.exists(data_with_predictions):
    if os_name == "Windows":
        os.system(f"start {data_with_predictions}")
    elif os_name == "Linux":
        os.system(f"xdg-open {data_with_predictions}")
    elif os_name == "Darwin":
        os.system(f"open {data_with_predictions}")
    else:
        print("Operator not known")
else:
    print("Error: CSV-file is not know, try running the program again.")
print("The CSV-file with the predicted prices is now opened.")
