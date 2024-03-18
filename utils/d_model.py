from utils.c_train import train_model
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def model(new_data):
    df_conc_test, df_conc_train, y_train, y_test = train_model()
    #choosing model:
    model = LinearRegression()
    model.fit(df_conc_train, y_train)
    y_pred= model.predict(df_conc_test)
    mse = mean_squared_error(y_test, y_pred)
    print("Mean Sqaured Error for this model is: ", mse)
    print(model.score(df_conc_test, y_test))

    return y_pred
