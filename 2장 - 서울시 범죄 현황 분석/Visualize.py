import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import platform
from sklearn import preprocessing

crime_anal_raw = pd.read_csv('02. crime_in_Seoul_include_gu_name.csv',
                            encoding='utf-8')
crime_anal_raw = pd.read_csv('02. crime_in_Seoul_include_gu_name.csv',
                            encoding='utf-8', index_col = 0)
crime_anal = pd.pivot_table(crime_anal_raw, index = '구별', aggfunc=np.sum)
    # 검거율 비율 발행
crime_anal['강간검거율'] = crime_anal['강간 검거']/crime_anal['강간 발생'] *100
crime_anal['강도검거율'] = crime_anal['강도 검거']/crime_anal['강도 발생'] *100
crime_anal['살인검거율'] = crime_anal['살인 검거']/crime_anal['살인 발생'] *100
crime_anal['절도검거율'] = crime_anal['절도 검거']/crime_anal['절도 발생'] *100
crime_anal['폭력검거율'] = crime_anal['폭력 검거']/crime_anal['폭력 발생'] *100
# 검거'율'이 있으니 '건수'는 필요 없으니까 지우기
del crime_anal['강간 검거']
del crime_anal['강도 검거']
del crime_anal['살인 검거']
del crime_anal['절도 검거']
del crime_anal['폭력 검거']
#  전년도 발생 건수에 대한 검거도 포함 되니 100으로 진행하기
con_list = ['강간검거율','강도검거율','살인검거율','절도검거율','폭력검거율']
for column in con_list:
    crime_anal.loc[crime_anal[column] > 100, column] = 100
# '발생'단어 지우기
crime_anal.rename(columns = {'강간 발생':'강간',
                            '강도 발생':'강도',
                            '살인 발생':'살인',
                            '절도 발생':'절도',
                            '폭력 발생':'폭력'}, inplace = True)
# 시각화 표현을 위한 '정규식'다듬기
col = ['강간','강도','살인','절도','폭력']
x = crime_anal[col].values
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x.astype(float))
# preprocessing.MinMacScaler()를 저장한 변수에다가
# 변수.fit_transform
crime_anal_norm = pd.DataFrame(x_scaled,
                                columns = col,
                                index = crime_anal.index)
col2 = ['강간검거율','강도검거율','살인검거율','절도검거율','폭력검거율']
crime_anal_norm[col2] = crime_anal[col2]

# 1장의 결과인  구별 인구수와 CCTV갯수 가져오기
result_CCTV = pd.read_csv('01. CCTV_result.csv',
                        encoding='UTF-8',
                        index_col='구별')

# 범죄 전체 데이터 합산
crime_anal_norm[['인구수','CCTV']] = result_CCTV[['인구수','소계']]

# 범죄 전체 데이터 합산
col = ['강간','강도','살인','절도','폭력']
crime_anal_norm['범죄'] = np.sum(crime_anal_norm[col], axis=1)

# 검거 전체 데이터 합산
col = ['강간검거율','강도검거율','살인검거율','절도검거율','폭력검거율']
crime_anal_norm['검거'] = np.sum(crime_anal_norm[col], axis=1)


crime_anal_norm.to_csv('2-8.범죄데이터 시각화하기 파일.csv',header=True, index=True,encoding='cp949')
