import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import numpy as np
import q4


test_points_2023 = pd.read_csv('test_points_2023.csv')
test_salary_2023 = pd.read_csv('test_salary_2023.csv')
data = test_salary_2023.merge(test_points_2023, left_on='NAME', right_on='name')

data['SALARY'] = data['SALARY'].astype(float)

predict_salary = q4.predict_salary(data[['ast', 'pts', 'fg3_pct']])

r_error = abs(predict_salary - data['SALARY']) / (predict_salary) * 100
print("The percentage of relative error less than 50% is " + str(len(r_error[r_error <= 50]) / len(r_error) * 100) + "%.")

predict_salary = q4.predict_salary_usecap(data[['ast', 'pts', 'fg3_pct']])

r_error = abs(predict_salary - data['SALARY']) / (predict_salary) * 100
print("The percentage of relative error less than 50% is " + str(len(r_error[r_error <= 50]) / len(r_error) * 100) + "%.")