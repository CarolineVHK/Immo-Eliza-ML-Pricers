# Model card

## Project context

In this repo you will see how I build up my machine learning model based on Linear Regression.  I used the data that we scraped and cleaned in previous projects.

## Data

I only selected the data for the PropertySubType 'House', from their I searched for the best variables to correlate with each other and choose to work with variables: 'Price', 'LivingArea','Province','BedroomCount'.

## Model details

Model I created works on Linear Regression.

## Performance

Performance metrics for the various models tested, visualizations, ...
Scores for Linear Regression Model for houses: 
    Score from train-set =  0.3479353658557168
    Score from test-set =  0.32490100588676196
Scores for RandomForestRegressor for houses: 
    Score train-set =  0.8304669318815453
    Score test-set =  0.8276332495649619

## Limitations

What are the limitations of your model?

## Usage

What are the dependencies, what scripts are there to train the model, how to generate predictions, ...

## Maintainers

Contributions to this project are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.