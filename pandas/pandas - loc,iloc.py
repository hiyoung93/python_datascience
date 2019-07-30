import pandas as pd
import numpy as np

# -------------------- 데이터프레임 고급 인덱싱
'''
- loc : label값 기반의 2차원 인덱싱
- iloc : 순서를 나타내는 정수 기반 2차원 인덱싱
- at : 라벨값 기반의 2차원 인덱싱(한개의 스칼라 값만 찾는다)
- iat : 순서 나타내는 정수 기반 2차원 인덱싱(한개의 스칼라 값을 찾는다)
'''

# ----------------------------------- loc인덱서
# df.loc[row index]
# df.loc[row index, columns index]
#
'''
- index data
- index data slicing
- index data list
- bool series(행 인덱싱의 경우)
- 위 값 반환 함수
'''

df = pd.DataFrame(np.arange(10,22).reshape(3,4),
                  index=['a','b','c'],
                  columns=['A','B','C','D'])
print(df)

# --------------------- 인덱싱 값을 하나만 받는 경우
'''
인덱스 하나만 넣으면 row선택 
index data가 'a'인 행을 고르면 행이 series로 출력됨
'''

print(df.loc['a'])
# ------------------- 슬라이싱 가능
print(df.loc['b':'c'])# == df['b':'c']
# ------------------- index data list 가능
print(df.loc[['b','c']]) # != df[['b','c']] 는 key error
# ------------------- bool series(행 인덱싱의 경우)
print(df.A > 14)
print(df.loc[df.A > 14])

# 인덱스 값 반환하는 함수로도 사용가능
def select_rows(df):
    return df.A > 15
print(select_rows(df))
print(df.loc[select_rows(df)])

# loc 인덱서가 없는 경우 라벨인덱싱,라벨리스트 인덱싱 불가
# df.loc['A'] == keyError
# df.loc[['A','B']] == keyError

df2 = pd.DataFrame(np.arange(10, 26).reshape(4, 4), columns=["A", "B", "C", "D"])
print(df2.loc[1:2])

# --------- 인덱싱 값을 행과 열 모두 받기
# df.loc[row, columns]
print(df.loc["a", :])
print(df.loc[["a", "b"], ["B", "D"]])
print(df.loc[df.A > 10, ["C", "D"]])

# -------------------------------------- iloc 인덱서
# 정수 인덱스만 받음
print(df.iloc[0, 1])
print(df.iloc[:2, 2])
print(df.iloc[0, -2:])
print(df.iloc[-1]) # 행 전체 선택

# -------------연습문제 1 ----------------------
# 1. 행과 열에 라벨을 가지는 5x5이상의 크기를 가지는 dataframe만들기
np.random.seed(34)
a = pd.DataFrame(np.random.randint(1, 30, size =(5, 5)),
                 index = ['a','b','c','d','e'],
                 columns=['A','B','C','D','E'])
print(a)
# 2. 10가지 이상의 방법으로 행, 열 선택하기
print(a.A)
print(a.B > a.D)
print(a.loc['a',: ])
print(a.iloc[2:4,0:3])
print(a.loc[a.E < 20,['A','C']])
print(a.loc['a','B'])
print(a.iloc[0:4])
print(a.iloc[-1:])
print(a.E)

