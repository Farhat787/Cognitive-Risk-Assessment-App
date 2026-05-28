# Dementia Risk Prediction App

A Streamlit-based machine learning application developed for the School of Nursing at the University of North Carolina Wilmington (UNCW). This application provides an interactive interface for testing a trained logistic regression pipeline model that estimates dementia risk probability based on survey and functional assessment variables.

## Overview

This project was created as part of a machine learning and health informatics initiative to explore how demographic, cognitive, wellbeing, and functional ability variables can be used to estimate dementia risk.

The application allows users to:

* Enter survey-based assessment information
* Generate a dementia risk prediction
* View the estimated probability of dementia
* Interact with a clean and user-friendly interface

The app is designed for educational, research, and demonstration purposes.

---

## Technologies Used

* Python
* Streamlit
* Scikit-learn
* Pandas
* Joblib

---

## Model Information

The deployed model is a trained logistic regression pipeline saved as:

```text
final_log_reg_pipeline_model.pkl
```

The model uses a combination of:

* Demographic variables
* Physical ability indicators
* Memory and cognitive assessment variables
* Wellbeing-related survey measures

The application displays human-readable survey labels while preserving the original encoded values required by the trained model.

---

## Live Application


---

## Deployment

This application is designed to be deployed using Streamlit Community Cloud.

---

## Project Structure

```text
├── app.py
├── final_log_reg_pipeline_model.pkl
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Disclaimer

This application is intended for academic, educational, and research demonstration purposes only. It is not intended for clinical diagnosis, medical decision-making, or patient treatment.

---

## Author

Farhat Joyan
University of North Carolina Wilmington (UNCW)
