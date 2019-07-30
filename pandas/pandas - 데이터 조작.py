import pandas as pd
import numpy as np
import seaborn as sns
# ------------------------ 데이터 갯수 세기
# count 사용, NaN 값은 세지 않음
s = pd.Series(range(10))
s[3] = np.nan
print(s)
print(s.count())
# 각 열마다 별도로 갯수 측정, 데이터에서 값이 누락된 부분을 찾을 때 유용
np.random.seed(3)
df = pd.DataFrame(np.random.randint(5, size = (4,4)),dtype=float)
df.iloc[2,3] = np.nan # 임의로 nan값 설정함
print(df)
print(df.count())
print(df[0].value_counts()) #
# ---------------------------------- 연습문제 4.2.5
# 타이타닉호 승객데이터의 데이터 값을 각 열마다 구해본다.
titanic = sns.load_dataset("titanic")
print(titanic.count)

# ---------------------- 카데고리 값 세기
# value_counts ; 값이 나온 횟수를 셀 수 있다.
np.random.seed(1)
s2 = pd.Series(np.random.randint(6, size=100))
s2.tail()
print(s2.value_counts())
# DataFrame 에는 value_counts가 없어서 열마다 별도로 적용해야함
print(df[0].value_counts())

# ----------------------------- 정렬
''' sort_index ; 인덱스 값 기준 정렬
 sort_values ; 데이터 값 기준 정렬

'''
print(s2.value_counts().sort_index())
print(s.sort_values())

# ---------------------------------- 연습문제 4.2.6
# sex, age, class, alive 인원수 구하기
print(titanic['sex'].value_counts())
print(titanic['age'].value_counts())
print(titanic['class'].value_counts())
print(titanic['alive'].value_counts())


# ---------------------------------- 연습문제 4.2.7
# 사망자와 생존자로 그룹 나누고 labels의 승객비율구하기
# 비율의 전체 합은 1 이 되어야 한다
bins = [1, 15, 25, 35, 60, 99]
labels = ["미성년자", "청년", "중년", "장년", "노년"]
