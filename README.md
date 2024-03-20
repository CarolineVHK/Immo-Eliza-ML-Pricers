# Real Estate Price Prediction in Belgium

[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## Table of Contents

- [Introduction](#introduction)
- [Mission](#mission)
- [Data](#data)
- [Preprocessing](#preprocessing)
- [Machine Learning Model](#machine-learning-model)
- [Repo Structure](#Repo Structure)
- [Timeline](#Timeline)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This repository contains code and documentation for a machine learning project aimed at predicting real estate prices in Belgium. The project was undertaken for Becode as a project to learn the ML skills.

## Mission

The mission of this project is to develop a robust machine learning model that can accurately predict real estate prices in Belgium. This involves several key steps:

1. **Data Collection**: Scraping real estate data from relevant sources, cleaning and analyzing the data to identify patterns and trends.

2. **Preprocessing**: Preprocessing the data to prepare it for training a machine learning model. This includes handling missing values, encoding categorical variables, and scaling numerical features.

3. **Machine Learning Model**: Building and training a machine learning model using the preprocessed data. The model should be capable of predicting real estate prices based on various features such as location, size, and amenities.

4. **Evaluation**: Evaluating the performance of the machine learning model using appropriate metrics and techniques. This ensures that the model is accurate and reliable.

## Data

The data used in this project is from the previous team-projects (https://github.com/CarolineVHK/immo-eliza-scraping-Python_Pricers - and https://github.com/CarolineVHK/immoeliza-analysis), which include various features such as location, size, number of bedrooms, and price. The dataset was collected through web scraping and contains both numerical and categorical variables.

## Preprocessing

The preprocessing step involves cleaning and transforming the raw data into a format suitable for training a machine learning model. This includes handling missing values, encoding categorical variables using one-hot encoding or label encoding, and scaling numerical features to a similar range.

## Machine Learning Model

The machine learning model used in this project is a Linear Regression Model, trained on the preprocessed data and this only for PropertySubType 'House'. The model is capable of predicting real estate prices based on the input features.

## Repo structure

```
.
├── data/
│ ├── raw_data.csv
│ ├── preprocessed_data.csv
│ ├── prediction_data.csv
├── models/
│ └── linear_regres_houses.pkl
├── utils/
│ ├── import_data.py
│ ├── preprocessing_data.py
│ ├── train.py
│ ├── model_for_linear_regression.py
│ ├── predict.py
│ ├── crossvalidation.py
├── .gitignore
├── predict.py
├── modelscard.md
├── README.md
├── requirements.txt
└── training_results.py
```

## ⏱️ Timeline

The development of this project took 5 days for completion.

## Usage

To use the code in this repository, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the program using `predict.py`

 This will execute the model, loading data `new_data.csv`, cleaning it, handling missing values and preproces the data for the model. When the model is finished a new csv-file called `predictions_new_data.csv` will be created and automatically open for you.

## Contributing

Contributions to this project are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project was completed as part of the AI Bootcamp at BeCode.org. 
Previous steps in this project (scraping data and cleaning data) was completed by the team Python Pricers.

---

