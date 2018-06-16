import matplotlib.pyplot as plt
import csv
x=[]
y=[]
with open('test.csv','r') as csvfile:
    plots=csv.reader(csvfile)#reads file
    for row in plots:        #accessing row by row
        x.append((row[0]))   #accessing first element of row
        y.append((row[1]))   #accessing 2nd element of row

plt.plot(x,y,label='File')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
