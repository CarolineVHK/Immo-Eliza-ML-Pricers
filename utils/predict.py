


def make_predictions(model, df):
    """
    Make predictions using the trained model.

    Parameters:
    - model: Trained machine learning model.
    - df: DataFrame containing the preprocessed new data.

    Returns:
    - predictions: Predicted values for the new data.
    """
    predictions = model.predict(df)

    return predictions
