from utils.d_model import model

new_data = input('Which dataframe do you want me to run for you? ')

predicted_prices = model(new_data)

print(predicted_prices)