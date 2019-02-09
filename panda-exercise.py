import pandas as pd
import numpy as np

dictionary = {"NAME": ["ali", "veli", "kenan", "hilal", "ayse", "evren"],
              "AGE": [15, 16, 17, 18, 19, 20],
              "MAAS": [100, 200, 300, 400, 500, 600]}

dataFrame1 = pd.DataFrame(dictionary)

head = dataFrame1.head()

tail = dataFrame1.tail()

print(dataFrame1.columns)
print(dataFrame1.info())
print(dataFrame1.dtypes)
print(dataFrame1.describe())

print(dataFrame1["AGE"])
print(dataFrame1.AGE)

dataFrame1["yeni_feature"] = [-1, -2, -3, -4, -5, -6]
print(dataFrame1.loc[:, "AGE"])
print(dataFrame1.loc[:3, "AGE"])

filter1 = dataFrame1.MAAS > 200

filtered = dataFrame1[filter1]

print(filtered)

filter2 = dataFrame1.AGE < 18

filtered = dataFrame1[filter1 & filter2]

print(filtered)



