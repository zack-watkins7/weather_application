import matplotlib.pyplot as plt
import pandas as pd

salary_data= pd.read_csv('Linear Regression\salary_data.csv')

yearsExperience= salary_data.YearsExperience
salary = salary_data.Salary

print(salary_data)


#Loss functions are important because it tell's us how off we are from the actual result.
def loss_function(m,b, points):
    n = len(points)
    total_error = 0
    for i in range(0,len(points)):
        x= points.iloc[i].yearsExperience
        y= points.iloc[i].salary

        total_error += (y-m*x+b)**2
    total_error / n
