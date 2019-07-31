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
# reset_index 사용시 drop = True 설정시 버려짐
df2 = df2.reset_index(drop=True)
print(df2)
