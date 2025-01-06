# Student Performance Prediction.

## Project Overview

This project aims to predict student performance using a regression task. We employed several regression models to determine which one performs the best on our dataset. Our analysis focused on evaluating the models based on their accuracy and other performance metrics.

## Dataset

The dataset used in this project contains various features that may influence student performance, such as:

- Gender

- Race / ethnicity

- Lunch

- Parental education level

- Test preparation course

- Reading score

- Writing score

- Math score

## Models Used

We implemented the following regression models for this task:

- Random Forest
- Decision Tree
- Gradient Boosting
- Linear Regression
- XGBRegressor
- CatBoosting Regressor
- AdaBoost Regressor

## Evaluation Metrics

To evaluate the performance of the models, we used the following metrics:

- Mean Absolute Error (MAE): Measures the average magnitude of errors in predictions.

- Mean Squared Error (MSE): Measures the average squared difference between observed and predicted values.

- Root Mean Squared Error (RMSE): Square root of MSE, providing a measure of the standard deviation of the prediction errors.

- R-squared (R²): Represents the proportion of the variance for the dependent variable that's explained by the independent variables.

## Results

After training and testing the models, we found that the Linear Regression model provided the best performance on our dataset, achieving the lowest MAE, MSE, and RMSE, and the highest R² score.
