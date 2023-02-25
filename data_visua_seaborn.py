# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 13:31:06 2021

@author: DELL
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

mtcars=pd.read_csv('mtcars.csv')
mtcars.columns
m=mtcars.rename( {'Unnamed: 0': 'Model'}, axis='columns')

##Statistical Data Visualization - 1 lineplot, 2 scatterplot
#syntax - seaborn.lineplot(x,y)

res = sn.lineplot(m['hp'],m['mpg'])
plt.show()

res = sn.lineplot(m['hp'],m['cyl'],hue=m['am'],style=m['am'])
plt.show()

res = sn.lineplot(m['hp'],m['mpg'],hue=m['gear'],style=m['gear'])
plt.show()


#Scatter plot syntax
#seaborn.scatterplot()
sn.scatterplot(m['hp'],m['cyl'])
sn.scatterplot(m['hp'],m['cyl'],hue=m['am'],style=m['am'])

#Categorical Data Visualization - Boxplot, boxen plot swarn , vilon
#Syntax---- seaborn.boxplot(),seaborn.boxenplot(),seaborn.violinplot(),seaborn.swarmplot()
res = sn.boxplot(m['mpg'])
plt.show()
sn.boxenplot(m['hp'])
'''Seaborn Violin Plot is used to represent the underlying data 
distribution of a data variable across its data values.'''
sn.violinplot(m['mpg'])
'''creates a swarm of data points around the data values that happen to repre
-sent a relationship between the two categorical data variables/columns.'''

sn.swarmplot(m['gear'],m['cyl'])
##Estimation plot
'''Seaborn Barplot represents the data distribution among the data variables 
as a frequency distribution of the central tendency values.'''
sn.barplot(m['cyl'],m['carb'])
sn.pointplot(m['carb'],m['cyl'])
sn.countplot(m['gear'])

#Univariant analysis
res=sn.distplot(data['mpg'])
plt.show()

#bivariant analysis
sn.kdeplot(data['mpg'],data['qsec'])

a=sn.pairplot(m)
a.savefig('pp.png')


