import seaborn as sns
import matplotlib.pyplot as plt
import platform
import pandas as pd
path = 'C:/Windows/Fonts/malgun.ttf'
from matplotlib import font_manager, rc

if platform.system() == 'Darwin':
    rc('font',family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font',family=font_name)
else:
    print('Unknown system...sorry')

crime_anal_norm = pd.read_csv('2-8.범죄데이터 시각화하기 파일.csv',encoding='cp949', index_col = 0)
print(crime_anal_norm)

plt.show()
sns.pairplot(crime_anal_norm, vars=['강도','살인','폭력'], kind='reg',size=6)

# CCTV갯수를 기준으로 좌측면에 살인과 강도의 높은 수를 갖는 데이터가 보인다
sns.pairplot(crime_anal_norm, x_vars=['인구수','CCTV'],
            y_vars=['살인','강도'], kind='reg',size=3)
plt.show()

# 살인 및 폭력 검거율과 CCTV관계는 음의 상관계수도를 보인다.
sns.pairplot(crime_anal_norm,
            x_vars=['인구수','CCTV'],
            y_vars=['살인검거율','폭력검거율'], kind='reg',size=3)
plt.show()

tmp_max = crime_anal_norm['검거'].max()
crime_anal_norm['검거'] = crime_anal_norm['검거'] / tmp_max * 100
crime_anal_norm_sort = crime_anal_norm.sort_values(by='검거',ascending=False)


# 검거율의 합계인 검거 항목 최고값을 100으로 한정 그 값을 정렬하고 heatmap으로 나타내기
# heatmap에서 cmap을 설정해줘야지 큰 숫자가 진해진다
# 합으로 된 정렬
target_col = ['강간검거율','강도검거율','살인검거율','절도검거율','폭력검거율']
crime_anal_norm_sort = crime_anal_norm.sort_values(by='검거',ascending=False)
plt.figure(figsize=(10,10))
sns.heatmap(crime_anal_norm_sort[target_col], annot=True, fmt='f',linewidths=.5, cmap =plt.cm.RdYlGn)
plt.title('범죄 검거 비율(정규화된 검거의 합으로 정렬)')
plt.show()


# 건수로 된 정렬
target_col = ['강간','강도','살인','절도','폭력','범죄']
crime_anal_norm['범죄'] = crime_anal_norm['범죄'] / 5
crime_anal_norm_sort = crime_anal_norm.sort_values(by='범죄', ascending=False)
plt.figure(figsize=(10,10))
sns.heatmap(crime_anal_norm_sort[target_col], annot=True, fmt='f', linewidths=.5, cmap=plt.cm.Blues)
plt.title('범죄비율 (정규화된 발생 건수로 정렬)')
plt.show()
