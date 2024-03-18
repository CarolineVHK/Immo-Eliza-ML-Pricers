
from utils.c_train import train_model
from sklearn.metrics import mean_squared_error
from utils.d_model import model

def make_predictions():
    """
    Make predictions using the trained model.

    Parameters:
    - model: Trained machine learning model.
    - X: DataFrame containing the features for prediction.

    Returns:
    - y_pred: Predicted values.
    """
    model()
    y_pred = model.predict(df_conc_test)
    mse = mean_squared_error(y_test, y_pred)
    print("Mean Sqaured Error for this model is: ", mse)
    print(model.score(df_conc_test, y_test))

    return y_pred