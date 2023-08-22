import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd

dataset = pd.read_csv('Position_Salaries.csv')
x = dataset.iloc[:,1].values
y = dataset.iloc[:, -1].values

print("levels :", x)
print("Salaries : ", y)

std_err = stats.linregress(x,y)

def myfunc(x):
    return slope*x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x,y)
plt.plot(x,mymodel)
plt.title('Salary vs Experience')
plt.xlabel('Years of experience')
plt.ylabel('Salary')
plt.show()
