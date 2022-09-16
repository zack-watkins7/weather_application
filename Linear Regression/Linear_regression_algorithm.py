import matplotlib.pyplot as plt
import pandas as pd

salary_data= pd.read_csv('Linear Regression\salary_data.csv')
print(salary_data)
yearsExperience= salary_data.YearsExperience
salary = salary_data.Salary
#Loss functions are important because it tell's us how off we are from the actual result.
def loss_function(m,b, points):
    n = float(len(points))
    total_error = 0
    for i in range(0,len(points)):
        x= points.iloc[i].YearsExperience
        y= points.iloc[i].Salary

        total_error += (y-m*x+b)**2
    total_error / n


def gradient_descent(m_now, b_now, points, L):
    m_gradient = 0
    b_gradient = 0

    n= len(points)

    for i in range(0,n):
        x= points.iloc[i].YearsExperience
        y= points.iloc[i].Salary
        m_gradient += -(2/n)*x*(y-(m_now*x+b_now))
        b_gradient += -(2/n)*(y-(m_now*x+b_now))

    m = m_now - m_gradient * L
    b = b_now - b_gradient * L

    return m, b

m=0
b=0
L=0.001
epochs = 100000

for i in range(epochs):
    m,b = gradient_descent(m,b,salary_data, L)
print(m,b)


plt.scatter(yearsExperience, salary , color="black")
plt.plot(list(range(2,30)), [m*x+b for x in range(2,30)], color= "red")
plt.show()
