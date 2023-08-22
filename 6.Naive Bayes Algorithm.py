import csv

# Read the dataset
a = []
with open('play_tennis.csv', 'r') as dataset:
    for i in csv.reader(dataset):
        a.append(i)
a.pop(0)  # Remove the header row

# Prompt user for attribute values of a new case
case = []
no_attributes = len(a[0]) - 1  # Subtract 1 instead of 2

for i in range(0, no_attributes):
    x = input("Attribute " + str(i + 1) + ": ")
    case.append(x)

print("The given case is: " + str(case))

# Calculate counts of positive and negative instances
positive = sum(1 for row in a if row[-1] == "Yes")
negative = len(a) - positive

print(positive)
print(negative)

# Calculate positive and negative probabilities
prob_pos = positive / len(a)
prob_neg = negative / len(a)

print(prob_pos)
print(prob_neg)

# Initialize Naive Bayes probabilities
NB_pos = prob_pos
NB_neg = prob_neg

# Calculate conditional probabilities
for i in range(0, no_attributes):
    count_pos = sum(1 for row in a if row[i] == case[i] and row[-1] == "Yes")
    count_neg = sum(1 for row in a if row[i] == case[i] and row[-1] == "No")
    
    x = count_pos / positive if positive > 0 else 0
    y = count_neg / negative if negative > 0 else 0
    
    NB_pos = NB_pos * x
    NB_neg = NB_neg * y

print(NB_pos)
print(NB_neg)

# Print classification result
if NB_pos > NB_neg:
    print(str(case) + " corresponds to YES")
else:
    print(str(case) + " corresponds to NO")

