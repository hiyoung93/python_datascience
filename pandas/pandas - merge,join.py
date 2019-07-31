import pandas as pd
import numpy as np
import seaborn as sns

df1 = pd.DataFrame({
    '고객번호' : [1001, 1002, 1003, 1004, 1005, 1006, 1007],
    '이름' : ['둘리','도우너','또치','길동','희동','마이콜','영희']
},  columns = ['고객번호','이름'])

df2= pd.DataFrame({
    '고객번호' : [1001, 1002, 1003, 1004, 1005, 1006, 1007],
    '금액' : [10000,20000,15000,500,50000,10000,2500]
}, columns = ['고객번호','금액'])

# merge d1,d2를 합치면 공통 기준으로 DataFrame찾아서 합친다
print(pd.merge(df1,df2))   # inner join 방식
print(pd.merge(df1,df2,how = 'outer'))   # outer join 방식

# ex ) 키값이 같은 데이터가 여러개 있을 땐 경우의 수를 따져서 조합만들기
df1 = pd.DataFrame({
    '품종' : ['setosa','setosa','virginica','virginica'],
    '꽃잎길이' : [1.4,1.3,1.5,1.3]},
    columns = ['품종','꽃잎길이'])
print(df1)

df2 = pd.DataFrame({
    '품종' : ['setosa', 'virginica','virginica','versicolor'],
    '꽃잎너비' : [0.4, 0.3, 0.5, 0.3]},
    columns = ['품종','꽃잎너비'])
print(df2)
print(pd.merge(df1,df2))

# 이거 아래쪽
# df1 ; 금액 나타태는 데이터, df2 ; 성별 나타내는 데이터
df1 = pd.DataFrame({
    '고객명' : ['근상','근상','준현'],
    '날짜' : ['2018-01-01','2018-01-02','2018-01-01'],
    '데이터' : ['20000','3000','42300']})

df2 = pd.DataFrame({
    '고객명' : ['근상','준현'],
    '데이터' : ['남자','여자']})
# 기준열이 아니면서 같은 이름을 가진 열은 _x, _y같은 접미사가 붙는다
print(pd.merge(df1,df2, on='고객명'))



# 기준열의 이름이 다르다면 left_on, right_on 을 사용해서 기준열을 명시
df1 = pd.DataFrame({
    '이름':['영희','철수','철수'],
    '성적':[1,2,3]})
df2 = pd.DataFrame({
    '성명':['영희','영희','철수'],
    '성적':[3,4,5]})
print(pd.merge(df1, df2, left_on = '이름',right_on='성명'))

# 인덱스를 기준열로 사용하려면 left_index, right_index인수를 True로 설정
df1 = pd.DataFrame({
    '도시' : ['서울','서울','서울','부산','부산'],
    '연도' : [2000,2005,2010,2000,2005],
    '인구': [9853972, 9762546, 9631482, 3655437, 3512547]})
df2 = pd.DataFrame(
    np.arange(12).reshape((6,2)),
    index=[['부산','부산','서울','서울','서울','서울'],
            [2000,2005,2000,2005,2010,2015]],
    columns=['데이터1','데이터2'])

print(pd.merge(df1,df2, left_on=['도시','연도'],right_index=True))


df1 = pd.DataFrame(
    [[1., 2.],[3., 4.],[5., 6]],
    index = ['a','c','e'],
    columns=['서울','부산'])

df2 = pd.DataFrame(
    [[7., 8.],[9., 10.],[11., 12.],[13., 14]],
    index=['b','c','d','e'],
    columns=['대구','광주'])
print(pd.merge(df1, df2, how='outer',left_index=True, right_index=True))



# ------------------------------------------- join

print(df1.join(df2, how ='outer'))

# ---------------------- 연습문제 4.2.10 ----------------
# 두개의 프레임을 merge로 합친다.
# 각각 조건, 1. 5X5이상의 크기, 2. 공통열 하나 이상, 공통열의 이름은 서로 다름
df1 = pd.DataFrame({
    '지역' : ['광주','서울','대전','서울','부산'],
    '사이즈' : [280,265,250,275,310],
    '키' : [184,186,173,185,178],
    '이름' : ['형준','희택','하영','선우','택'],
    '수입' : [250,350,230,500,280]})

df2 = pd.DataFrame({
    '성명' : ['형준','희택','하영','선우','택'],
    '수입': [280,265,250,275,310],
    '키' : [184,186,173,185,178],
    '거짓말' : ['잘가','가지마','행복해','떠나지마','뿅'],
    '가수' : ['쏜','흥','민','박효신','최고']})

print(pd.merge(df1,df2, how='outer',left_on='이름',right_on="성명"))

# ------------------------------------------ concat 사용 데이터 연결
# 단순 데이터 연결만 함, 단순연결이기에 값이 중복됨

s1 =pd.Series([0,1], index=['A','B'])
s2 =pd.Series([0,2,4], index=['A','B','C'])
print(pd.concat([s1,s2]))


# 옆으로 연결시에는 axis = 1 인수 설정
df1 =pd.DataFrame(
    np.arange(6).reshape(3,2),
    index = ['a','b','c'],
    columns = ['데이터1','데이터2'])
df2 = pd.DataFrame(
    5 + np.arange(4).reshape(2,2),
    index = ['a','c'],
    columns=['데이터3','데이터4'])
print(pd.concat([df1,df2], axis=1,sort=False))

# -------------------------- 연습문제 4.2.11 ------------
jaju = pd.DataFrame({
    '매출' : [500,200],
    '비용' : [100,100],
    '이익' : [400,100]})
jude = pd.DataFrame({
    '매출' : [500,200],
    '비용' : [100,100],
    '이익' : [400,100],
    '년도' : [2018,2019]})
print(pd.concat([jaju,jude],axis=1,sort=True))
