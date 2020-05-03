### Simple Linear Regression

#### Key take-aways from summary of Ordinary Least Square (OLS from statsmodel.api)

1. Dep. Variable - Dependent variable
2. Coefficient - Intercept value and coefficient value for each dependent variable to build the regression equation
3. p-value
    - If p-value < 0.05, independent variable has an impact on dependent variable (Null hypothesis is rejected here)
    - Otherwise, can be removed from the regression analysis
4. R-squared
    - Ranges from 0 to 1 (Practical range - 0.2 to 0.9)
    - 0 means No variability and 1 means entire variability
    - Higher value means, higher explanatory power of the model (which is good)
    - If value is less, it means we are missing dependent variables to be part of the model
5. Adj. R-squared
    - Adjusted R-square is smaller than R-square
    - Penalizes excessive use of variables
    - More accurate measure of model performance
    - Must be high number
6. F-statistic
7. Prob (F-statistic)
    - Must be as small as possible (almost 0)
8. Durbin-Watson - Fall between the range of 0 to 4.
    - If value < 1 or value > 3, dependent and independent variables are auto-correlated (not good)
    - If value == 2, not auto-correlated (good)
    - Solution - When in presence of auto-correlation, avoid linear regression model. Use an alternative model like
    auto-regressive model or moving average model, auto-regressive [integrated] moving average model

##############################################################################

                            OLS Regression Results
==============================================================================
Dep. Variable:                    GPA   R-squared:                       0.406
Model:                            OLS   Adj. R-squared:                  0.399
Method:                 Least Squares   F-statistic:                     56.05
Date:                Fri, 20 Sep 2019   Prob (F-statistic):           7.20e-11
Time:                        00:19:43   Log-Likelihood:                 12.672
No. Observations:                  84   AIC:                            -21.34
Df Residuals:                      82   BIC:                            -16.48
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.2750      0.409      0.673      0.503      -0.538       1.088
SAT            0.0017      0.000      7.487      0.000       0.001       0.002
==============================================================================
Omnibus:                       12.839   Durbin-Watson:                   0.950
Prob(Omnibus):                  0.002   Jarque-Bera (JB):               16.155
Skew:                          -0.722   Prob(JB):                     0.000310
Kurtosis:                       4.590   Cond. No.                     3.29e+04
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 3.29e+04. This might indicate that there are
strong multicollinearity or other numerical problems.
##############################################################################
