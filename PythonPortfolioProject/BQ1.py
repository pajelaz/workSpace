"""
Zachary Pajela

Business Question: How can we create visuals that help represent the unequal pay woman have to men?





"""

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inc = pd.read_csv(__location__ + '/income_threshold.csv')

#plt.bar(inc.sex, inc.)
plt.show()
