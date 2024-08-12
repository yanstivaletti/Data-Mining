# -*- coding: utf-8 -*-
"""Survival challenge template.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12R2vzLwOGWvLf94BjRGVIcxYMHwSQhwS

# Libraries
"""

!pip install lifelines

#libraries
import pandas as pd
import statsmodels.api as sm

"""#Data"""

#import the dataset
dataset = sm.datasets.get_rdataset("solder",
                                   package = "survival").data

dataset.head()

#Transform survival variable
import numpy as np
dataset["Solder"] = np.where(
    dataset["Solder"] == "Thin", 1, 0)

"""# Kaplan Meyer estimator"""

#Kaplan-Meier Estimator
from lifelines import KaplanMeierFitter
model = KaplanMeierFitter()
model.fit(durations = dataset["skips"], 
          event_observed = dataset["Solder"])

#plotting survival
import matplotlib.pyplot as plt
model.plot(figsize = (12,8))
plt.xlabel("Skips")

"""#Log Rank test"""

dataset.Panel.unique()

#log rank test
from lifelines.statistics import multivariate_logrank_test
logrank = multivariate_logrank_test(
    dataset["skips"],
    dataset["Panel"],
    dataset["Solder"])
print(logrank)