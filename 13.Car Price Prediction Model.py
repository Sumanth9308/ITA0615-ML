import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.tree import plot_tree

# Import the dataset
data = pd.read_csv("CarPrice.csv")

# Checking if NULL values exist
data.isnull().sum()

# Exploring the dataset
print(data.info())
print(data.describe())
print(data.CarName.unique())

sns.set_style("whitegrid")

# Using displot or histplot instead of deprecated distplot
plt.figure(figsize=(15, 10))
sns.displot(data.price, kde=True)  # or sns.histplot(data.price, kde=True)
plt.show()

# Drop non-numeric columns and calculate correlations
correlation_data = data.drop(['CarName', 'fueltype'], axis=1)  # Remove 'fueltype'
correlations = correlation_data.corr()

plt.figure(figsize=(20, 15))
sns.heatmap(correlations, cmap="coolwarm", annot=True)
plt.show()

# One-hot encode categorical variables
data = pd.get_dummies(data, columns=['fueltype'], drop_first=True)

# Split the data into features and target
predict = "price"
data = data[["symboling", "wheelbase", "carlength", 
             "carwidth", "carheight", "curbweight", 
             "enginesize", "boreratio", "stroke", 
             "compressionratio", "horsepower", "peakrpm", 
             "citympg", "highwaympg", "fueltype_gas",  # Add one-hot encoded column
             "price"]]

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)

model = DecisionTreeRegressor(random_state=42)
model.fit(xtrain, ytrain)
predictions = model.predict(xtest)

# Evaluate the model using R^2 score and MAE
r2 = r2_score(ytest, predictions)
mae = mean_absolute_error(ytest, predictions)
print(f"R^2 Score: {r2}")
print(f"Mean Absolute Error: {mae}")

# Visualize the Decision Tree
plt.figure(figsize=(20, 15))
plot_tree(model, feature_names=data.columns[:-1], filled=True, rounded=True)
plt.show()
