# -*- coding: utf-8 -*-
"""Dimension Reduction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BWxGaJNM4TRgPTRn03uHEAPG_Hfhih2T

# Data and libraries
"""

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive/Data Mining for Business in Python 2021/5. Dimension Reduction

#import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA

#import dataset
dataset = pd.read_csv("houses_to_rent.csv")
dataset.head()

#transform strings into dummy
dataset[["animal", "furniture"]] = pd.get_dummies(dataset[["animal", "furniture"]],
                                                  drop_first = True)
dataset.head()

"""# Correlation Matrix"""

#Isolate X
X = dataset.drop(columns = 'rent amount')
X.head(1)

#Correlation Matrix
import seaborn as sns
sns.heatmap(X.corr(),
            annot = True,
            fmt = '.1g',
            center = 0,
            cmap = 'coolwarm',
            linewidths = 1,
            linecolor = 'black')

"""#Standardize data"""

#Standardization
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns = X.columns)
X_scaled.head()

"""# Principal Component Analysis"""

#Optimal number of components
model = PCA(random_state=1502).fit(X_scaled)
plt.plot(model.explained_variance_ratio_,
         linewidth = 4)
plt.xlabel('Components')
plt.ylabel('Explained Variance')
plt.show()

#cumulative
plt.plot(np.cumsum(model.explained_variance_ratio_),
         linewidth = 4)
plt.xlabel('Components')
plt.ylabel('Explained Variance Cumulative')
plt.show()

#PCA
model = PCA(n_components=4,
            random_state = 1502).fit(X_scaled)

#Interpretation 
model_interpretation = pd.DataFrame(model.components_,
                                    columns = X.columns)
model_interpretation

#components
components = model.transform(X_scaled)
components = pd.DataFrame(components,
                          columns = ['city characteristics',
                                     'accepts animals and has furniture',
                                     'rural small place',
                                     'fantastic houses'])
components.head()

#merge the dataset
final_dataset = pd.concat([components, dataset], axis = 1)
final_dataset.head()

"""#Manifold Learning"""

#t-SNE
from sklearn.manifold import TSNE
model = TSNE(n_components = 2,
             random_state = 1503)
components = model.fit_transform(X)
components

#Plotting
plt.scatter(components[:,0],
            components[:,1],
            cmap = "hsv",
            c = dataset["rent amount"])
plt.title("t-SNE scatter plot")
plt.show()