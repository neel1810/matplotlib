# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 12:16:33 2020

@author: DELL
"""

from matplotlib import pyplot as plt
import numpy as np
import math #needed for definition of pi
np.arange(10)
x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)
plt.plot(x,y)
plt.plot(x,np.cos(x),'m-.')
plt.xlabel("angle")
plt.ylabel("sine")
plt.title('sine wave')
plt.show()

from numpy import *
from pylab import *
x = linspace(-3, 3, 30)
y = x**2
plot(x, y)
show()
## Multiplots
from pylab import *
plot(x, sin(x))
plot(x, cos(x), 'r-')
plot(x, -sin(x), 'g--')
show()
## setting axis
from matplotlib import pyplot as plt
import numpy as np
import math
x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)

'''fig2=plt.figure()
aa=fig2.add_axes([0,-1,12,1])
aa.plot(x,np.sin(x),'rD')
aa.plot(x,np.cos(x),'yo')'''

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.set_title("sine wave")
ax.set_xlabel('angle')
ax.set_ylabel('sine')
plt.show()
help(plt.plot)
### feature plot
import matplotlib.pyplot as plt
y = [1, 4, 9, 16, 25,36,49, 64]
x1 = [1, 16, 30, 42,55, 68, 77,88]
x2 = [1,6,12,18,28, 40, 52, 65]
fig = plt.figure()
ax = fig.add_axes([0,0,1,2])
l1 = ax.plot(x1,y,'rs-') # solid line with yellow colour and square marker
l2 = ax.plot(x2,y,'yo--') # dash line with green colour and circle marker
ax.legend(labels = ('tv', 'Smartphone'), loc = 'lower right') # legend placed at lower right
ax.set_title("Advertisement effect on sales")
ax.set_xlabel('medium')
ax.set_ylabel('sales')
plt.show()

plot(x, y, color='green', marker='o', linestyle='dashed',
            linewidth=2, markersize=0.2)

## plot inside plot
import matplotlib.pyplot as plt
import numpy as np
import math
x = np.arange(0, math.pi*2, 0.05)
fig=plt.figure()
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
axes2 = fig.add_axes([0.55, 0.55, 0.3, 0.3]) # inset axes
y = np.sin(x)
axes1.plot(x, y, 'b')
axes2.plot(x,np.cos(x),'r')
axes1.set_title('sine')
axes2.set_title("cosine")
plt.show()

##setting ticks
import matplotlib.pyplot as plt
import numpy as np
import math
x = np.arange(0, math.pi*2, 0.05)
fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
y = np.sin(x)
ax.plot(x, y)
ax.set_xlabel('angle')
ax.set_title('sine')
ax.set_xticks([0,2,4,6])
ax.set_xticklabels(['zero','two','four','six'])
ax.set_yticks([-1,0,1])
plt.show()

## Bar plots
lab=[1,2,3,4,5]
b=[12,23,45,67,29]
plt.bar(lab,b)
plt.barh(lab,b)

langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23,17,35,29,12]
plt.bar(langs,students)

data = [[30, 25, 50, 20],
[40, 23, 51, 17],
[35, 22, 45, 19]]
X = np.arange(4)
plt.bar(X + 0.00, data[0], color = 'm', width = 0.25)
plt.bar(X + 0.25, data[1], color = 'g', width = 0.25)
plt.bar(X + 0.50, data[2], color = 'y', width = 0.25)
plt.xticks(X,list('ABCD'))

##Stack plot
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
ind = np.arange(5) # the x locations for the groups
w = 0.35

plt.bar(ind, menMeans, w, color='r')
plt.bar(ind, womenMeans, w,bottom=menMeans, color='b')
plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend(labels=['Men', 'Women'])
plt.show()
##pie plot
plt.pie(b,explode=[0,0.15,0,0,0],labels=lab,autopct='%1.2f%%')
plt.pie(students, labels = langs,autopct='%1.2f%%')
import pandas as pd
mtcars=pd.read_csv(r"D:\mtcars.csv")
import matplotlib.pyplot as plt
import numpy as np

print(mtcars.gear)
val=pd.value_counts(mtcars.gear)
plt.pie(val,autopct='%1.2f%%',explode=[0,0,0.2])
## histogram
a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
plt.hist(a)
plt.hist(a, bins = [0,25,50,75,100])
plt.title("histogram of result")
plt.xticks([0,25,50,75,100])
plt.xlabel('marks')
plt.ylabel('no. of students')
##boxplot
np.random.seed(10)
collectn_1 = np.random.normal(100, 10, 200)
collectn_2 = np.random.normal(80, 30, 200)
collectn_3 = np.random.normal(90, 20, 200)

plt.boxplot([collectn_1,collectn_2,collectn_3])
plt.violinplot([collectn_1,collectn_2,collectn_3])


## Scatter plot
import matplotlib.pyplot as plt
girls_grades = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
boys_grades = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
grades_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.scatter(grades_range, girls_grades, color='r')
ax.scatter(grades_range, boys_grades, color='b')
ax.set_xlabel('Grades Range')
ax.set_ylabel('Grades Scored')
ax.set_title('scatter plot')
plt.show()
