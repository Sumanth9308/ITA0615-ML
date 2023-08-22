import csv

num_attributes = 0  
version_space = []  

# Load data from CSV file
with open('climate.csv', 'r') as dataset:
    reader = csv.reader(dataset)
    a = list(reader)
    num_attributes = len(a[0]) - 1

s = ['0'] * num_attributes
g = ['?'] * num_attributes

version_space.append(g.copy()) 

# Iterate through the training data
for i in range(len(a)):
    if a[i][num_attributes] == 'yes':
        print("Instance " + str(i + 1) + " +ve ")
        for j in range(num_attributes):
            if s[j] == '0' or s[j] == a[i][j]:
                s[j] = a[i][j]
            else:
                s[j] = '?'
        version_space.append(s.copy())  
        print("S" + str(i + 1), s)
        print("G" + str(i + 1), version_space[-1]) 
    elif a[i][num_attributes] == 'no':
        print("Instance " + str(i + 1) + " -ve ")
        print("S" + str(i + 1), s)
        for j in range(num_attributes):
            if s[j] != a[i][j] and s[j] != '?':
                g[j] = s[j]
        version_space.append(g.copy())  
        g = ['?'] * num_attributes  
        print("G" + str(i + 1), version_space[-1])
    print()

print("Final Version Space:", version_space)
