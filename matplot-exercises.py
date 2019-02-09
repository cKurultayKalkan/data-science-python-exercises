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

# plot
import matplotlib.pyplot as plt

df1 = df.drop(["Id"], axis=1)
print(df1)

df1.plot()
plt.show()

setosa = df[df.Species == "Iris-setosa"]
versicolor = df[df.Species == "Iris-versicolor"]
virginica = df[df.Species == "Iris-virginica"]

plt.plot(setosa.Id, setosa.PetalLengthCm, color="red", label="setosa")
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color="green", label="versicolor")
plt.plot(virginica.Id, virginica.PetalLengthCm, color="blue", label="virginica")
plt.legend()
plt.xlabel('Id')
plt.ylabel('Petal Length Cm')
df1.plot(grid=True, linestyle=":", alpha=0.5)
plt.show()
