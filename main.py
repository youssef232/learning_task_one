import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
# 1. Read the dataset, convert it to DataFrame and display some from it.

# print("1. Read the dataset, convert it to DataFrame and display some from it.")
# dataset = pd.read_csv("Wuzzuf_Jobs.csv")
# print(dataset)

# print("2. Display structure and summary of the data")
# print(dataset.describe())
#
# # 3. Clean the data (null, duplications)
#
# print("3. Clean the data (null, duplications)")
#
# dataset.sort_values(by=["Title", "Company", "Location", "Type", "Level", "YearsExp", "Country", "Skills"], inplace=True)
# dataset.drop_duplicates(subset=["Title", "Company", "Location", "Type", "Level", "YearsExp", "Country", "Skills"], keep="first", inplace=True)
# x = dataset.iloc[:, :].values
#
# from sklearn.impute import SimpleImputer
#
# imp_mean = SimpleImputer(missing_values=None, strategy='most_frequent')
# imp_mean = imp_mean.fit(x[:, :])
# x[:, :] = imp_mean.transform(x[:, :])
# print(x)
# 4 & 5. Count the jobs for each company and display that in order (What are the
# most demanding companies for jobs?)
# temp = dataset['Title']
# y = temp.value_counts()
# print(y)
# plt.pie(y)
# plt.show()

# 6 & 7
# dataset = pd.read_csv("Wuzzuf_Jobs.csv")
# x = dataset.iloc[500:550,0:1]
# y = x.value_counts()
# print(y)
# # fig = plt.figure(figsize=(5,2))
# y.plot.bar( color='blue')
# plt.xlabel("Titles")
# plt.ylabel("No. of titles")
# plt.title("what are the most popular job titles")
# plt.show()

# 8, 9

# dataset = pd.read_csv("Wuzzuf_Jobs.csv")
# x = dataset.iloc[0:50, 2:3]
# y = x.value_counts()
# print(y)
# y.plot.bar(color='pink', width=0.4, fontsize=8)
# plt.xlabel("Areas")
# plt.ylabel("No. of people")
# plt.title("Most Areas")
# plt.show()

# 10

# dataset = pd.read_csv("Wuzzuf_Jobs.csv")
#
# x = dataset.iloc[:, len(dataset.columns) - 1:len(dataset.columns)]
# y=x.value_counts()
# print(y)
