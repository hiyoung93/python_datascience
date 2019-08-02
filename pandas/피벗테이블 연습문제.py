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

#
# iris = sns.load_dataset('iris')
# print(iris)
# ir = iris.groupby(iris.species).mean()
# print(ir[['sepal_width','sepal_length']])


# ----------------------------------------- 연습문제 3
# tips = sns.load_dataset('tips')

# 1. 요일, 점심/저녁/인원수의 영향을 받는지 확인하기

# print(tips.groupby(['day','time'])[['size']].describe())

# 2. 어떠한 요인이 가장 크게 작용하는 판단 방법있는가
# describe로 전체 통계값을 확인하고 day,time별로 묶는다
#

# ----------------------------------------- 연습문제 4
# 타이타닉 승객 분석
titanic = sns.load_dataset('titanic')

# 1. qcut 명령으로 나이 그룹 만들기
df = titanic['who'].unique() # columns 데이터 확인하기


titanic['age_group']= pd.qcut(titanic.age, 3, labels=['child','mid','old'])
print(titanic.head())


# 2. 성별, 선실, 나이 생존율을 데이터 프레임 계산,
# row - sex, 나이그룹, columns - 선실


# 3. 성별 및 선실에 의한 생존율 pivot_table형태로 만들기
