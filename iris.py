import pandas as pd
import matplotlib.pyplot as plt
import csv
x=[]
y=[]
df=pd.read_csv("C:/Users/hp/Desktop/data/iris.csv")
print(df)
print(df.describe())
print(df['SepalLengthCm'])
x.append(df['SepalLengthCm'])
y.append(df['PetalLengthCm'])
plt.scatter(x,y,label="stars",color="green",marker='*',s=30)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('my first graph')
plt.show()




