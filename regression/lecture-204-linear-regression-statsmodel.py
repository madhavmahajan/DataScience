"""
Lecture - 204 (categorical data)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns   # seaborn is used to beautify graphs plotted by matplotlib
sns.set()               # set() method will enable seaborn

file_name = "./data/1.03. Dummies.csv"
data = pd.read_csv(file_name)

print("-" * 80)
print("Raw data from the csv file")
print(data.head())

# Handle categorical data by assigning a numerical value for each category
data['Attendance'] = data['Attendance'].map({'Yes': 1, 'No': 0})

print("-" * 80)
print("Data after handling categorical data")
print(data.head())

print("-" * 80)
print("Description of raw data")
print(data.describe(include='all'))

y = data['GPA']
x1 = data[['SAT', 'Attendance']]

x = sm.add_constant(x1)
results = sm.OLS(y, x).fit()
print("-" * 80)
print("Summary of the results for OLS")
print(results.summary())

const_coeff, sat_coeff, attendance_coeff = results.params
print("-" * 80)
print("Coefficients generated from the regression algorithm:")
print("1.   Constant coeff - {}".format(const_coeff))
print("2.        SAT coeff - {}".format(sat_coeff))
print("3. Attendance coeff - {}".format(attendance_coeff))

print("-" * 80)
print("Scatter plot with prediction as per the regression model")
plt.scatter(data['SAT'], y, c=data['Attendance'], cmap="RdYlGn_r")
yhat_overall = const_coeff + sat_coeff * data['SAT'] # + attendance_coeff * data['Attendance']
fig = plt.plot(data['SAT'], yhat_overall, lw=4, c='orange', label='yhat')
plt.show()

print("-" * 80)
print("Scatter plot with prediction involving attendance")
plt.scatter(data['SAT'], y, c=data['Attendance'], cmap="RdYlGn_r")
# yhat_overall = const_coeff + sat_coeff * data['SAT'] + attendance_coeff * data['Attendance']
yhat_yes = const_coeff + sat_coeff * data['SAT'] + attendance_coeff
yhat_no = const_coeff + sat_coeff * data['SAT']
# fig = plt.plot(data['SAT'], yhat_overall, lw=4, c='orange', label='yhat')
fig = plt.plot(data['SAT'], yhat_yes, lw=4, c='green', label='yhat')
fig = plt.plot(data['SAT'], yhat_no, lw=4, c='red', label='yhat')
plt.show()

