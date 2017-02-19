from __future__ import division, print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pygal
data = pd.read_csv('2016-first-quarter-citations.csv')

#Dropping rows that has any missing values
data = data.dropna(how='any')
data.shape

#getting Age into a list
age=data['Cited Person Age']
#maximum age
max(age)

#minimum age
min(age)

#Creating the tuples (height,start location,end location) for the Pygal Histogram)
#From the 0 to the maximum value of Age (0,117)
agelist=[0]*120
for a in age:
    agelist[int(a)]+=1

agetuples=[]
for age in range(0,117):
    agetuples.append((agelist[age],age,age+1))

hist = pygal.Histogram(title=u'Histogram of Citations across Age - Q1 2016', x_title='Age',y_title="Total Citations",show_legend=False,tooltip_border_radius=10)
hist.add("Age Histogram", agetuples[:116])
hist.render_to_file('ageHistogram-corrected.svg')from __future__ import division, print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('2016-first-quarter-citations.csv')

#Dropping rows that has any missing values
data = data.dropna(how='any')
data.shape

#getting Age into a list
age=data['Cited Person Age']
#maximum age
max(age)

#minimum age
min(age)

#Creating the tuples (height,start location,end location) for the Pygal Histogram)
#From the 0 to the maximum value of Age (0,117)
agetuples=[]
for age in range(0,117):
    agetuples.append((agelist[age],age,age+1))

hist = pygal.Histogram(title=u'Histogram of Citations across Age - Q1 2016', x_title='Age',y_title="Total Citations",show_legend=False,tooltip_border_radius=10)
hist.add("Age Histogram", agetuples)
hist.render_to_file('ageHistogram.svg')
