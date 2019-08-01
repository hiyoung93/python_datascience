import pandas as pd
import numpy as np
import seaborn as sns


# ----------------------------------------- 연습문제 1
# key1값을 기준으로 data1값을 분류해서 합계를 구하고 결과를 데이터프레임으로 구한다
\
# a = df2.groupby(df2.key1).sum()['data1']
# a = pd.DataFrame(a)
# print(type(a))


# ----------------------------------------- 연습문제 2
# species별로 꽃잎길이(sepal_length), 꽃잎 폭(sepal_width)평균 구하기
# 종이 표시 되지 않을결루 종을 찾아 낼수 있는가?
# mean, median, min, max - 그룹데이터의 평균, 중앙값, 최소, 최대
# sum, prod, std, var, quantile - 그룹데이터의 합계, 곱, 표준편차, 분산, 사분위수


iris = sns.load_dataset('iris')
print(iris)
ir = iris.groupby(iris.species).mean()
print(ir[['sepal_width','sepal_length']])
