import pandas as pd
import joblib
from preprocessing import clean_select_data

linregr = joblib.load('models/lin_regres_houses.pkl')
new_data = pd.read_csv('data/new_data.csv')

clean_select_data(new_data)
df = pd.read_csv('data/preprocessed_data.csv')
predictions = linregr.predict(df)

#save into file:
predictions_df = pd.DataFrame(predictions, columns=['Predicted_Price'])
predictions_df.to_csv('predictions_new_data.csv', index=False)