import pandas as pd
import numpy as np
import seaborn as sns
# ---------------------------- 시계열 자료 다루기
# datatimeindex
'''
pd.to_datetime 함수 ; 날짜/ 시간 문자열로 자동 변경, datetimeIndex 자료형으로 생성됨
pd.date_range 함수

'''

date_str = ['2018, 1,, 1', '2018, 1, 4', '2018, 1, 5', '2018, 1, 6']
idx = pd.to_datetime(date_str)
print(idx)


np.random.seed(3)
s = pd.Series(np.random.randn(4), index = idx)
print(s)

# pd.date_range함수를 쓰면 모든 날짜/ 시간을 입력하면 범위내의 인덱스를 생성해 준다

print(pd.date_range('2018-4-1', '2018-4-30'))

print(pd.date_range(start ='2018-4-1',periods=30))

# --------------------------------------freq로 특정 날짜만 생성,
'''   pd.date_range('처음','끝', 원하는 함수)
freq인수 값은 다음과 같다
http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases
'''
# freq = 'B' 주말이 아닌 평일만
print(pd.date_range('2018-4-1','2018-4-30',freq='B'))

# freq='W' 주 의 일요일만
print(pd.date_range('2018-1-1','2018-12-31', freq='W'))

# freq='W-MON' 월요일만
print(pd.date_range('2018-1-1','2018-12-31',freq='W-MON')
