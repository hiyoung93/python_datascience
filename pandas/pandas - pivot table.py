import pandas as pd
import seaborn as sns
# ----------------------------------- pivot table
'''
pivot_table(data, values = None, index = None, Cloumns = None, aggfunc = 'mean',
            fill_value = None, margins = False, margins_name = 'All')

 - data - 분석할 dataframe
 - values - 분석할 dataframe의 열
 - index - 행 인덱스로 들어갈 키 열, 키 열의 리스트
 - columns - 열 인덱스로 들어갈 키 열, 키 열의 리스트
 - aggfunc - 분석메서드
 - fill_value - NaN 대체 값
 - margins - 데이터 분석한 결과를 오른쪽& 아래 붙일지 여부
 - margins_name - 마진 열(행)의 이름
'''

data = {
    "도시": ["서울", "서울", "서울", "부산", "부산", "부산", "인천", "인천"],
    "연도": ["2015", "2010", "2005", "2015", "2010", "2005", "2015", "2010"],
    "인구": [9904312, 9631482, 9762546, 3448737, 3393191, 3512547, 2890451, 263203],
    "지역": ["수도권", "수도권", "수도권", "경상권", "경상권", "경상권", "수도권", "수도권"]
}
columns = ["도시", "연도", "인구", "지역"]
df1 = pd.DataFrame(data, columns=columns)

# dataframe으로 데이터가 있어야지 pivot_table을 생성할 수 있다.
# 변수명.pivot_table('데이터','행','열')
print(df1.pivot_table('인구','도시','연도'))


# margins=True 를 주면 aggfunc처럼 분석 방법을
# 해당 행렬의 모든데이터 에 적용한 결과를 같이 보여줌 aggfunc가 없으면 평균계산하기
print(df1.pivot_table("인구", "도시", "연도", margins=True, margins_name="합계"))

# 행,열에 리스트를 넣어서 다중 index table만들기
# index를 추가하면 row들을 groupby시켜줌
print(df1.pivot_table('인구', index=['연도','도시']))
print(df1.pivot_table('인구', index=['도시','연도']))


# ------------------------------------------ 데이터 예제
''' ------------------ seaborn내제 데이터
total_bill: 식사대금
tip: 팁
sex: 성별
smoker: 흡연/금연 여부
day: 요일
time: 시간
size: 인원
'''
tips = sns.load_dataset('tips')
print(tips.tail())

# ------------------------- 식사대금대비 팁 비율
tips['tip_pct'] = tips['tip'] / tips['total_bill']
print(tips.tail())
# 각 열 데이터의 분포 알아보기
print(tips.describe())

# ------------------- 그룹별 통계
print(tips.groupby('sex').count()) # nan데이터가 없다면 전체적으로 동일하게 표시된다.
print(tips.groupby('sex').size()) # nan데이터가 있어도 상관하지 않고, 더 간단하게 표시됨
# 흡연유무로 나누기
# 변수명.groupby(['columns1','columns2'])
print(tips.groupby(['sex','smoker']).size())

# 보기 좋게 바꾸기
# aggfunc - 분석메서드
# margins - 데이터 분석한 결과를 오른쪽& 아래 붙일지 여부
print(tips.pivot_table('tip_pct','sex','smoker',aggfunc='count',margins=True))

# ------------------- 성별과 흡연 여부에 따른 평균 팁 비율 살피기
# [['tip_pct']] 아까 만들어놓은 변수
# 순서 잘 생각하기
print(tips.groupby('sex')[['tip_pct']].mean())
# [] 를 하나만 하면 columns의 이름이 보이지 않는다
# print(tips.groupby('sex')['tip_pct'].mean())

print(tips.groupby('smoker')[['tip_pct']].mean())

# pivot_table으로 진행
# 변수명. pivot_table('데이터==columns name','row')
print(tips.pivot_table("tip_pct", "sex"))

# 변수명.pivot_table('데이터',['row','groupby'])
print(tips.pivot_table("tip_pct", ["sex", "smoker"]))

# 변수명.pivot_table('데이터','row','columns')
print(tips.pivot_table("tip_pct", "sex", "smoker"))

# ---------------- describe로 여러 통계값 한번에 알아보기
# 변수명.pivot_table('row')[[데이터]]describe
print(tips.groupby('sex')[['tip_pct']].describe())


# 변수명.pivot_table('row')[[데이터]]describe
print(tips.groupby('smoker')[['tip_pct']].describe())


# 변수명.pivot_table('row')[[데이터]]describe
print(tips.groupby(['sex','smoker'])[['tip_pct']].describe())


# ---------------------------------------팁의 차이를 알아보자
# 그룹연산의 함수가 없으므로 함수를 직접만들고 agg메서드를 사용

# 여기서 x의 정체를 잘 모르겠음..
def peak_to_peak(x):
    return x.max() - x.min()
# tips.groupby(['row','==명'])[['columns명']].agg(함수)
print(tips.groupby(['sex','smoker'])[['tip']].agg(peak_to_peak))

# 그룹연산 동시에 하기
# 변수명.groupby(['row','==명']).agg(['columns명',만든 함수])[['columns의 groupby']]
print(tips.groupby(['sex','smoker']).agg(['mean', peak_to_peak])[['total_bill']])

# 열마다 다른 연산을 하고 싶으면 열 라벨과 연산이름(함수)를 dict에 넣는다
# 변수명.groupby(['row','==명']).agg(['columns1': 연산1,'columns2': 연산2])
print(tips.groupby(['sex','smoker']).agg(
    {'tip_pct' : 'mean', 'total_bill':peak_to_peak}))

print(tips.pivot_table('size',['time','sex','smoker'],'day',
                        aggfunc = 'sum', fill_value=0))
