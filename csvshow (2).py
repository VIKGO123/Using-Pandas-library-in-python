import matplotlib.pyplot as plt
import csv
x=[]
y=[]
with open('test.csv','r') as csvfile:
    plots=csv.reader(csvfile)
    for row in plots:
        x.append((row[0]))
        y.append((row[1]))

plt.plot(x,y,label='file')
plt.xlabel('x')
plt.ylabel('y')
plt.show
