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