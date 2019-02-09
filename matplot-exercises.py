"""
Created on 9 Feb 2019

@author: Çağdaş Kurultay Kalkan
"""

# mathplotlib

import pandas as pd

df = pd.read_csv("iris.csv")
print(len(df))
print(df.columns)
print("**********")
print(df.Species.unique())
print("**********")
print(df.info())
print("**********")
print(df.describe())

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
print(setosa.describe())
print(versicolor.describe())
