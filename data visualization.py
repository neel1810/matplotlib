# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 03:59:18 2019

@author: DELL
"""

import pandas as pd
import matplotlib.pyplot as plt
mtcars = pd.read_csv("D:\\Livewire Training\\Data Science and Machine Learning\\R Scripts\\R Script Topic Wise\\mtcars.csv")



import seaborn as sns 
# getting boxplot of mpg with respect to each category of gears 
sns.boxplot(x="gear",y="mpg",data=mtcars)
help(sns.boxplot)
sns.pairplot(mtcars.iloc[:,0:2]) # histogram of each column and 
# scatter plot of each variable with respect to other columns 

import numpy as np
plt.plot(np.arange(32),mtcars.mpg) # scatter plot of single variable

plt.plot(np.arange(32),mtcars.mpg,"ro-")

help(plt.plot) # explore different visualizations among the scatter plot
help(pd.merge)
# Scatter plot between different inputs

plt.plot(mtcars.mpg,mtcars["hp"],"ro");plt.xlabel("mpg");plt.ylabel("hp")

mtcars.hp.corr(mtcars.mpg)
mtcars.corr()
# ro  indicates r - red , o - points 
# 
# group by function 
mtcars.mpg.groupby(mtcars.gear).median() # summing up all mpg with respect to gear

mtcars.cyl.value_counts()
# pie chart
mtcars.gear.value_counts().plot(kind="pie")

mtcars.mpg.groupby(mtcars.gear).plot(kind="line")
mtcars.gear.plot(kind="pie")
# bar plot for count of each category for gear 
mtcars.gear.value_counts().plot(kind="bar")


# histogram of mpg for each category of gears 
mtcars.mpg.groupby(mtcars.gear).plot(kind="hist") 
mtcars.mpg.groupby(mtcars.gear).count()

# line plot for mpg column
mtcars.mpg.plot(kind='line') 
plt.plot(np.arange(32),mtcars.mpg,"ro-")


mtcars.mpg = mtcars.mpg.astype(str)
mtcars.gear = mtcars.gear.astype(str)
mtcars.groupby(mtcars.gear).count()

mtcars.groupby("gear")["mpg"].apply(lambda x: x.mean())

mtcars.gear.value_counts().plot(kind="pie")
mtcars.gear.value_counts().plot(kind="bar")

mtcars.head()

pd.crosstab(mtcars.gear,mtcars.cyl).plot(kind="bar",stacked=False,grid=True)
plt.scatter(mtcars.mpg,mtcars.wt)
mtcars.plot(kind="scatter",x="mpg",y="wt")
mtcars.mpg.plot(kind="hist")

import seaborn as sns
sns.pairplot(mpg,hue="gear",size=3,diag_kind = "kde")

sns.FacetGrid(mtcars,hue="cyl").map(plt.scatter,"mpg","wt").add_legend()
sns.boxplot(x="cyl",y="mpg",data=mtcars)
sns.FacetGrid(mtcars,hue="cyl").map(sns.kdeplot,"mpg").add_legend()

sns.pairplot(mtcars,hue="gear",size=3)
