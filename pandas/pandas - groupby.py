import pandas as pd
import numpy as np
import seaborn as sns
# ------------------------------- pivot table
'''
1 번째 인수 ; 행 인덱스 - 사용할 열 이름

2 번째 인수 ; 열 인덱스 - 사용할 열 이름
'''

data = {
    "도시": ["서울", "서울", "서울", "부산", "부산", "부산", "인천", "인천"],
    "연도": ["2015", "2010", "2005", "2015", "2010", "2005", "2015", "2010"],
    "인구": [9904312, 9631482, 9762546, 3448737, 3393191, 3512547, 2890451, 263203],
    "지역": ["수도권", "수도권", "수도권", "경상권", "경상권", "경상권", "수도권", "수도권"]
}
columns = ["도시", "연도", "인구", "지역"]
df1 = pd.DataFrame(data, columns=columns)
print(df1)

# --------------------------------- 알기 쉽게 pivot table만들기
print(df1.pivot('도시','연도','인구'))
# 변수명.pivot('행','열','데이터') ---- 데이터가 없는 곳은 NaN값 표시된다.
# 행 과 열은 데이터를 찾는 키 역할을 한다.
# 데이터의 값은 '단 하나' 만 찾아져야 한다.
# 행열의 값이 두개 이상이면 에러가 난다.

# ---------------------------------------- 그룹 분석
'''
키 지정조건에 맞는 데이터가 하나 이상이라면 행렬의 특성을 보여주는 : group analysis
1. 분석하고자하는 Series, DataFrame에 groupby 호출해서 그룹화 한다.
2. 그룹 연산 수행
'''
# -------------------------------- groupby : 그룹별로 분류
# 열또는 열의 리스트
# 행인덱스
''' --------------------------- 그룹연산 메서드 -------------
size, count - 그룹 데이터 갯수
mean, median, min, max - 그룹데이터의 평균, 중앙값, 최소, 최대
sum, prod, std, var, quantile - 그룹데이터의 합계, 곱, 표준편차, 분산, 사분위수
first, last - 그룹데이터의 첫번째, 마지막 데이터
agg, aggregate - 원하는 그룹연산이 없을시, agg전달
               - 연산을 동시에 하고플때, 이름 문자열의 리스트 전달
describe - 여러개의 값을 dataframe으로 구하기
apply - 원하는 그룹연산이 없을 때 사용
transform - 그룹별 계산을 통해서 데이터 자체를 변경함
'''

np.random.seed(3)
df2 = pd.DataFrame({
    'key1' : ['A','A','B','B','A'],
    'key2' : ['one','two','one','two','one'],
    'data1' : [1,2,3,4,5],
    'data2' : [10,20,30,40,50]})
print(df2)
print('--------------------------------------------------------------------')

# groupby를 사용해서 그룹 A와 그룹 B로 구분한 데이터를 만든다.
groups = df2.groupby(df2.key1)
print(groups)

# groupby 객체에는 데이터 인덱스를 저장한 group 속성이 있다.
print(groups.groups)

# A,B 그룹의 합계구하기(sum)
print(groups.sum())

# 위 과정을 명시적으로 얻을 필요가 없을시 연속 호출 가능
print(df2.data1.groupby(df2.key1).sum())

# 그룹분석한 결과에서 원하는 데이터만 뽑을수 있다.
# Group클래스객체에서 data1만 선택분석하는경우
print(df2.groupby(df2.key1)['data1'].sum())

# 전체 데이터를 분석 '후' data1만 선택한 경우
print(df2.groupby(df2.key1).sum()['data1'])

print('--------------------------------------------------------------------')


# ------------------ 키 값에 따른 data1합계 구하기.
# 분석하고자하는 키가 복수이면 리스트사용
print(df2.data1.groupby([df2.key1, df2.key2]).sum())

# unstack으로 pivot table형태를 만들 수 있다.
print(df2.data1.groupby([df2['key1'], df2['key2']]).sum().unstack('key2'))

# 지역별 합계 가능
print(df1['인구'].groupby([df1['지역'], df1['연도']]).sum().unstack('연도'))


print('--------------------------------------------------------------------')



# ------------------------------------------- iris data가지고 놀기
''' 사용 메서드
agg, aggregate - 원하는 그룹연산이 없을시, agg전달
               - 연산을 동시에 하고플때, 이름 문자열의 리스트 전달
describe - 여러개의 값을 dataframe으로 구하기
apply - 원하는 그룹연산이 없을 때 사용
'''

iris = sns.load_dataset('iris')

# 종류별 큰값, 작은값 비율 합계구하기
def peak_to_peak_ratio(x):
    return x.max() / x.min()
print(iris.groupby(iris.species).agg(peak_to_peak_ratio))

# ------------------------- describe 기술통계적 값 구해줌
# 사용시 하나의 데이터 프레임이 생성된다

print(iris.groupby(iris.species).describe().T)

# top3 뽑아 내기
print('---------------------------------------------------------------------')

def top3_petal_length(df):
    return df.sort_values(by='petal_length', ascending=False)[:3]

print(iris.groupby(iris.species).apply(top3_petal_length))

# 그룹별 계산후 데이터프레임으로 추출
'''transform - 그룹별 계산을 통해서 데이터 자체를 변경함'''
def q3cut(s):
    return pd.qcut(s, 3, labels =['소','중','대'])

iris['petal_length_class'] = iris.groupby(iris.species)['petal_length'].transform(q3cut)

print(iris[['petal_length', 'petal_length_class']].tail(10))
