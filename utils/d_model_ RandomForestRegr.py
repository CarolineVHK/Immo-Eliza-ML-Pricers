from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from .train import train_model

def train_random_forest(X_train, y_train, num_estimators=100, max_depth=None, random_state=None):
    """
    Train a Random Forest model for regression.

    Parameters:
    - X_train: DataFrame or array-like containing the features for training.
    - y_train: Series or array-like containing the target variable for training.
    - num_estimators: Number of trees in the forest (default=100).
    - max_depth: Maximum depth of the trees (default=None).
    - random_state: Random seed for reproducibility (default=None).

    Returns:
    - model: Trained Random Forest model.
    """
    model_RFR = RandomForestRegressor(n_estimators=num_estimators, max_depth=max_depth, random_state=random_state)
    model_RFR.fit(X_train, y_train)

    df_conc_test, df_conc_train, y_train, y_test = train_model()
    y_pred= model_RFR.predict(df_conc_test)
    mse = mean_squared_error(y_test, y_pred)
    print("Mean Sqaured Error for this model is: ", mse)
    print("Score = ", model_RFR.score(df_conc_test, y_test))

    return model_RFR