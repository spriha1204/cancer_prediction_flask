Breast Cancer Predictor

A Flask web app that predicts whether a breast tumor is benign or malignant, using a logistic regression model trained on the Breast Cancer Wisconsin (Diagnostic) dataset.

How it works

The app takes six cell nucleus measurements via interactive sliders and returns a prediction from the trained model.

Features used: smoothness_mean, compactness_mean, concave points_mean, symmetry_mean, fractal_dimension_mean, symmetry_worst

These were chosen after removing highly correlated features (radius, perimeter, area, concavity) to avoid multicollinearity.

Tech Stack


Backend: Flask, scikit-learn (Logistic Regression + StandardScaler)
Frontend: HTML/CSS/JS
Dataset: Breast Cancer Wisconsin (Diagnostic)


Accuracy

~94% on the test set.
