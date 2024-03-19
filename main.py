from utils.model_for_linear_regression import model_LR
from utils.preprocessing import clean_select__data
import pandas as pd

print('One moment, the model is calculating the predictions...')

#launching the model:
predicted_prices = model_LR() #---> this is an array, need to change

#path for csv
data_with_predictions = "./data/prediction_data.csv"
#save the df predicted_prices to CSV file
pd.DataFrame(predicted_prices, columns=['Predicted_Price']).to_csv(data_with_predictions, index=False)
