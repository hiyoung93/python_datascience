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

del crime_anal['강간 검거']
del crime_anal['강도 검거']
del crime_anal['살인 검거']
del crime_anal['절도 검거']
del crime_anal['폭력 검거']

crime_anal.rename(columns = {'강간 발생':'강간',
                            '강도 발생':'강도',
                            '살인 발생':'살인',
                            '절도 발생':'절도',
                            '폭력 발생':'폭력'}, inplace = True)

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
crime_anal_norm.head()

path = 'THE_Oegyeinseolmyeongseo.ttf'
from matplotlib import font_manager, rc

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font',family=font_name)
else:
    print('Unknown system... sorry!')

sns.pairplot(crime_anal_norm, vars=['강도','살인','폭력'], kind='reg', size=3)
plt.show()
