# https://datascienceschool.net/view-notebook/ee0a5679dd574b94b55193690992f850/
import pandas as pd
# pandas 패키지 - 데이터 분석 사용할때 많이 쓰임,
# Series 클래스와 dataframe 클래스 제공

# ------------------------ Series = 값(Value) + 인덱스(Index)
# 리스트, 1차원 배열 형식으로 Series클래스 생성자에 넣어주면 시리즈 클래스 객채 생성
# index길이와 data의 길이는 같아야 함 index값==index label --- 문자, 날짜, 시간, 정수 가능
s = pd.Series([9904312, 3448737, 2890451, 2466052],
              index=["서울", "부산", "인천", "대구"])
print(s)
# 인덱스를 지정 안할시 인덱스는 0부터 시작하는 정수값
print(pd.Series(range(10, 14)))
# index는 속성으로 접근 가능, Series의 값은 1차원 배열 Values 속성접근 가능
print(s.index)
s.name = '인구'
s.index.name = '도시'
print(s)
# -------------------------------- Series연산
# 연산은 Series의 값만 적용, 인덱스 값은 변하지 않음.
# index값,label에는 영향 없음

print(s/ 1000000)
# ------------------------------- Series 인덱싱
# 슬라이싱가능
print(s[1],s['부산'])
print(s[3],s['대구'])

# 배열인덱싱을 하면 자료순서 바꾸기, 특정자료선택 가능
print(s[[2,3,1]])
print(s[['서울','대구','부산']])
print(s[(250e4< s ) & (s < 500e4)])

# 문자열 라벨 슬라이싱(:)기호 뒤에 오는 인덱스에 해당하는 값도 같이 설정
print(s[1:3])
print(s['부산':'대구'])

# 라벨값이 영문이면 (.) 이용해서 접근가능
s0=pd.Series(range(3),index=['a','b','c'])
print(s0)
print(s0.a)

# series == dict자료형
# label값을 key로 가지는 dict자료형과 같다.
print('서울' in s) # ---------bool 형
print('대전' in s)

# 즉, dict제공하는 in 연산가능 item메서드 사용시 for문으로 key, value접근가능
for k, v in s.items():
    print('%s = %d' % (k,v))

# dict을 series로 만들수 있음
s2 = pd.Series({"서울": 9631482, "부산": 3393191, "인천": 2632035, "대전": 1490158})
print(s2)
# 원소 순서 가리지 않음, 순서 지정원한다면 인덱스를 리스트로 지정
s2 = pd.Series({"서울": 9631482, "부산": 3393191, "인천": 2632035, "대전": 1490158},
               index=['부산','서울','인천','대전'])
print(s2)
# ------------------------------------ index기반 연산
# ------------------------------------ 인구증가 계산하기
ds = s - s2
print(ds)

print(s.values - s2.values)
# array([ 6511121, -6182745,   258416,   975894])


# NaN값이 float자료형에서만 가능, float자료형이 된다는 점을 주의
# NaN 아닌값을 구하려면 notnull메서드 사용
print(ds.notnull())
print(ds[ds.notnull()])

rs = (s - s2) / s2 * 100 # (s에서 s2빼고) 나누기 (s2 * 100)
rs = rs[rs.notnull()] # nan값 빼고rs 에 넣기
print(rs)

# ----------------------------------- 데이터 갱신, 추가, 삭제
# 인덱싱이 가능하면 갱신, 추가, 삭제 가능
rs['부산'] = 1.63
print(rs)
rs['대구'] = 1.41
print(rs)

del rs['서울']
print(rs)

# --------------------------- 연습문제1
# 1. 임의의 두개의 시리즈객체 생성, 문자열 index가지기, 공통적으로 포함되지 않는 라벨
a = pd.Series([3,5,6,7], index = ['안녕','반가워','저리가','바보야'])
b = pd.Series([3,5,6,7], index = ['안녕','반가워','저리가','바보야'])
print(a)
# 2. 두 시리즈 객체를 이용해서 사칙연산 만들기
a - b

