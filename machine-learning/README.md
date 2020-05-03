## Machine Learning

### Types
1. Supervised
2. Unsupervised
3. Reinforcement

### Building blocks of ML algorithm
1. Data
2. Model
3. Objective Function
4. Optimization Algorithm

### Supervised machine learning

#### Types
1. Classification
 - Categorization of data
2. Regression
 - Prediction of data

#### Linear Model
Equation - y = x*w + b
here, w - Weight of variable 'x'
      b - Bias

Also, x and w, both are vectors. x is of size nx1 and w is of size 1xn.
'n' being the size of x and w, is the number of inputs in the equation.

There is possibility of generating 2 outcomes from a single model, for which
above euqation can be adjusted by making 'y' and 'b' vectors as well.
In general, if we have 'k' inputs and 'm' outputs, weight matrix would be of
size kxm and bias would be of 1xm.

To generalize,
	y = x * w + b
here,
	y - nxm - Output matrix
	x - mxk - Input matrix
	w - kxm - Weight
	b - 1xm - Bias

### Objective Function
2 types:
1. Loss/Cost function
	- Deals with supervised learning algorithms
2. Reward function
	- Generally used in reinforcement algorithms

#### Loss function
Types:
1. L2-norm
	- Used in regression (supervised learning) algorithm 
	- Method to calculate - OLS (Euclidean distance between target and model
	  output)
2. Cross-entropy
	- Used in classification (supervised learning) algorithm

#### Algorithm
1. Gradient Descent





