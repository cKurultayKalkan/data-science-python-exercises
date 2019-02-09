import pandas as pd
import numpy as np

dictionary = {"NAME": ["ali", "veli", "kenan", "hilal", "ayse", "evren"],
              "AGE": [15, 16, 17, 18, 19, 20],
              "SALARY": [100, 200, 300, 400, 500, 600]}

dataFrame1 = pd.DataFrame(dictionary)

head = dataFrame1.head()

tail = dataFrame1.tail()

print(dataFrame1.columns)
print(dataFrame1.info())
print(dataFrame1.dtypes)
print(dataFrame1.describe())

print(dataFrame1["AGE"])
print(dataFrame1.AGE)

dataFrame1["new_feature"] = [-1, -2, -3, -4, -5, -6]
print(dataFrame1.loc[:, "AGE"])
print(dataFrame1.loc[:3, "AGE"])

filter1 = dataFrame1.SALARY > 200

filtered = dataFrame1[filter1]
print(filtered)

filter2 = dataFrame1.AGE < 18
filtered = dataFrame1[filter1 & filter2]
print(filtered)

average = dataFrame1.SALARY.mean()
print(average)

average_np = np.mean(dataFrame1.SALARY)
print(average_np)

dataFrame1["salary_level"] = ["high" if salary > average else "low" for salary in dataFrame1.SALARY]
print(dataFrame1)

dataFrame1.columns = [each.lower() for each in dataFrame1.columns]
print(dataFrame1)

dataFrame1.drop(["new_feature"], axis=1, inplace=True)
print(dataFrame1)

data1 = dataFrame1.head()
data2 = dataFrame1.tail()

# vertical
data_concat = pd.concat([data1, data2], axis=0)
print(data_concat)

# horizontal
salary = dataFrame1.salary
age = dataFrame1.age
data_h_concat = pd.concat([salary, age], axis=1)
print(data_h_concat)
