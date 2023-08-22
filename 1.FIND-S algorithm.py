import csv
import os
a=[]
attributes = ["Sky", "AirTemp", "Humidity", "Wind", "Water", "Forecast"]
specific_hypothesis = ['0'] * len(attributes)
csv_filename = input("Enter the CSV filename (e.g., training_data.csv): ")
with open(csv_filename, 'r') as csvfile:
    lines = csvfile.readlines()
    for line in lines[1:]:
        instance = line.strip().split(',')
        if instance[-1] == "Yes":
            for i in range(len(attributes) - 1):
                if specific_hypothesis[i] == '0':
                    specific_hypothesis[i] = instance[i]
                elif specific_hypothesis[i] != instance[i]:
                    specific_hypothesis[i] = '?'
print("Most specific hypothesis:", specific_hypothesis)
