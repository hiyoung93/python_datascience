import numpy as np
import pandas as pd

# --------------------------- 인덱스 설정 및 제거
# set_index ; 행 인덱스 제거, 데이터 열 중 하나를 인덱스로 설정
# reset_index ; 행 인덱스 제거, 인덱스를 데이터 열로

np.random.seed(2)
df1 = pd.DataFrame(np.vstack([list('ABCDE'),
                                np.round(np.random.rand(3,5),2)]).T,
                    columns=['C1','C2','C3','C4'])
print(df1)
# set_index ; C1열을 인덱스로 설정, 기존 인덱스 없어짐

df2 = df1.set_index('C1')
print(df2)

# C2열로 인덱스를 지정, 기존 인덱스 없어짐
df2 = df2.set_index('C2')
print(df2)

# reset_index ;  인덱스 열은 자료열의 선두로 삽입,
# 데이터프레임 인덱스틑 정수로 된 인덱스로 변경됨

df2 = df2.reset_index()
print(df2)
# reset_index 사용시 drop = True 설정시 기존 인덱스 버려짐
df2 = df2.reset_index(drop=True)
print(df2)

# ----------------------------------- 연습문제 1

# 1. 5명의 국,영,수 점수 만들기, 학생이름 열 포함하지 않기,
# df_score1 명을 가진 DataFrame생성
# df_score1.index 명에 학생이름 지정 index생성
# reset_index 로 df_score1.index을 일반 데이터열로 바꾸어서 df_score2 만들기

np.random.seed(34)

df_score1 = pd.DataFrame(np.random.randint(50, 100, size =(5, 3)))
print(df_score1)

df_score1.index = ['하영','선우','용후','세영','희택']
df_score1.columns = ['국어','수학','영어']
print(df_score1)

df_score2 = df_score1.reset_index()
print(df_score2)


# 2. df_score2 에 set_index로 학생이름 나타내는 인덱스 변경

df_score2 = df_score2.set_index('index')
print(df_score2)
