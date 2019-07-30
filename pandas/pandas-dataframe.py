# https://datascienceschool.net/view-notebook/ee0a5679dd574b94b55193690992f850/
import pandas as pd
import numpy as np

# ---------------------- 데이터 프레임 클래스 -------------------------
# Series ; 1차원 벡터 , dataframe ; 2차원 행렬 데이터
# dataframe은 row index와 column index 를 붙인다. (like excel)
# ------------------------------------- 데이터 프레임 생성 방법
# 1. 데이터를 리스트나 일차원 배열로 준비
# 2. 각각의 label을 key로 가지는 dict 생성
# 3. dataframe 클래스 생성자 넣기, 열방향 인덱스 = columns, 행방향 인덱스 = index
data = {
    "2015": [9904312, 3448737, 2890451, 2466052],
    "2010": [9631482, 3393191, 2632035, 2431774],
    "2005": [9762546, 3512547, 2517680, 2456016],
    "2000": [9853972, 3655437, 2466338, 2473990],
    "지역": ["수도권", "경상권", "수도권", "경상권"],
    "2010-2015 증가율": [0.0283, 0.0163, 0.0982, 0.0141]
}
columns = ["지역", "2015", "2010", "2005", "2000", "2010-2015 증가율"]
index = ["서울", "부산", "인천", "대구"]
df = pd.DataFrame(data, index=index, columns=columns)
print(df)
# 데이터만 접근하려면 values속성 사용,
# columns, index로 접근
print(df.values) # values 값만 가지고옴
print(df.columns) # 열 만 가지고 옴
print(df.index) # 행 만 가지고 옴

# 행열의 이름 붙이는것 가능
df.index.name = '도시'
df.columns.name = '특성'
print(df)
# ----------------------------------- 연습문제
# 1. 열 갯수와 행의 갯수가 각각 5개 이상
# 2. 열에는 정수, 문자열, 실수, 자료형 데이터 1개씩 포함
#
# df = {
#     '104': [34, 56, 74, 34],
#     '451': [45.1, 51.4, 4.57, 34],
#     '541': ['df', 'sd', 'ef', 'as'],
#     '12': [34, 56, 74, 34],
# }
# columns = ['104','451','541','12']
# index = ['워','라','벨','췍']
# frame = pd.DataFrame(df,index=index, columns=columns)
# print(frame)


# 전치(transpose)포함, Numpy 2차원 배열이 가지는 대부분의 속성 지원
print(df.T)
# --------------------------------------- 열 데이터 갱신, 추가, 삭제
df['2010-2015 증가율'] = df['2010-2015 증가율'] * 100
print(df)

df["2005-2010 증가율"] = ((df["2010"] - df["2005"]) / df["2005"] * 100).round(2)
print(df)
del df["2010-2015 증가율"]
print(df)

# ---------------------------------------- 열 인덱싱
# dataframe은 columns Series == dict
# 인덱싱할때 값을 하나만 넣으면 시리즈로 반환
print(df['지역'])
# 부분적인 프레임 반환도 가능
print(df[['2010','2015']])
# 자료형유지를 원하면 리스트써서 인덱싱
print(df[['2010']])
print(type(df[['2010']]))
print(df['2010'])
print(type(df['2010']))
# dataframe의 columns가 문자열 라벨일 경우, 정수로 인덱싱 불가.
# row가 문자열일때는 인덱싱은 가능
# 다만, 문자열이 아닌 정수형columns일때는 인덱스값을 정수로 사용가능
df2 = pd.DataFrame(np.arange(12).reshape(3,4))
print(df2[3])
# ------------------------------------- 행 인덱싱
# 행단위로 인덱싱을 하려한다면 항상 슬라이싱 하기
# 인덱스 값이 문자여도, 슬라이싱 가능
print(df[:1])
print(df[1:2])
print(df[1:3])
# --------------------------------------- 개별 데이터 인덱싱
# dataframe에서 열 라벨로 시리즈 인덱싱을 하면 시리즈,
# 시리즈를 다시 행 라벨로 인덱싱하면 개별 데이터가 됨
print(df['2015']['서울'])


# ----------------------- 연습문제3 -------Series&dataframe---------------------------
data = {
    "국어": [80, 90, 70, 30],
    "영어": [90, 70, 60, 40],
    "수학": [90, 60, 80, 70],
}
columns = ["국어", "영어", "수학"]
index = ["춘향", "몽룡", "향단", "방자"]
df = pd.DataFrame(data, index=index, columns=columns)
print(df)
# 1. 수학점수를 Series로 나타내기
print(df['수학'])
print(type(df['수학']))
# 2. 국어, 영어 점수를 dataframe으로 나타내기
print(df[['국어','영어']])
print(type(df[['국어','영어']]))
# 3. 모든 학생들의 각 과목 평균 점수를 새로운 열로 추가
df['평균점수'] = (((df['국어']+df['영어']+df['수학'])/3)).round(2)
print(df)
# 4. 방자의 영어 점수를 80점으로수정, 평균점수 다시 계산
eng = pd.DataFrame({'영어':[80]},index=['방자'])
df.update(eng)
df['평균점수'] = (((df['국어']+df['영어']+df['수학'])/3)).round(2)
print(df)
# 5. 춘향이의 점수를 dataframe으로 나타내기
print(df[:1])
print(type(df[:1]))

# 6. 향단이의 점수를 Series로 나타내기
print(df[2:3])