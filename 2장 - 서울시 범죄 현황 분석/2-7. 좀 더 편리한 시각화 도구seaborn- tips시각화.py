import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
# seaborn 연습 데이터
sns.set_style('whitegrid')

tips=sns.load_dataset('tips')
print(tips.head())

# 요일별 : 점심, 저녁, 흡연여부, 식사금액, 팁
plt.figure(figsize=(8,6))
sns.boxplot(x='day',y='total_bill', data=tips)
plt.show()

plt.figure(figsize=(8,6))
sns.boxplot(x='day',y='total_bill',hue='smoker',data=tips,palette='Set3')
plt.show()

sns.set_style('darkgrid')
sns.lmplot(x='total_bill',y='tip', data=tips, height=7)
plt.show()

sns.lmplot(x='total_bill',y='tip',hue='smoker',data=tips, palette='Set1',height=7)
plt.show()


#데이터 가져오기
flights = sns.load_dataset('flights')
print(flights.head())
#데이터 전처리
flights = flights.pivot('month','year','passengers')
print(flights.head())
# cmap을 설정해야지 높은 값이 진하게 나온다.
plt.figure(figsize=(10,8))
sns.heatmap(flights, annot=True, fmt='d', cmap='RdPu')
#sns.heatmap(변수, annot=True는 색상안에 데이터 쓰기)
plt.show()

# iris데이터를 가지고 놀기
sns.set(style='ticks')
iris = sns.load_dataset('iris')
print(iris.head())

sns.pairplot(iris, hue='species')
plt.show()
