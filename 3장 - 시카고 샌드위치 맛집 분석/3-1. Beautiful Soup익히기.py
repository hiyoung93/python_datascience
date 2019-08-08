from bs4 import BeautifulSoup
page = open('data/03. test_first.html','r').read()
soup = BeautifulSoup(page, 'html.parser')
print('===================================================')

# prettify() 를 사용하면 들여쓰기가 되서 보기가 좋다
print(soup.prettify())
# 변수.children을 사용하면 하나단계 아래에 포함 되어 있는 아이들을 보여준다
print(list(soup.children))
print('===================================================')

# html태그 접속을 원하면
html = list(soup.children)[2]
print('===================================================')

# 다시 html에 children을 넣어본다
print(list(html.children))
print('===================================================')

# html의 children중 3번을 찾아보면 body태그가 나타난다.
body = list(html.children)[3]
print(body)
# children과 parent를 이용해서 태그조사를 할 수 있다.
print('===================================================')
# 한번에 나타내기
print(soup.body)
print('===================================================')
# 바로 찾아내기
print(list(body.children))

print('===================================================')
# 찾아야하는 태그를 알고 있다면 find이나 find_all 을 많이 사용헌다
# 전체를 찾을때는 find_all
print(soup.find_all('p'))
print('===================================================')

# 하나만 찾을 때는 find
# find은 하나만 찾아 주기 때문에 다른 방법을 사용해야한다.
print(soup.find('p'))
print('===================================================')

# p태그의 class가 outer_text인것을 찾는 것도 가능하다
print(soup.find_all(class_='outer-text'))
# == soup.find_all(class_='outer-text')
print('===================================================')

# id로 찾기
print(soup.find_all(id='first'))
print('===================================================')

# head위치에 있는 body태그로 접근할수 있다.
print(soup.head.next_sibling.next_sibling)
print('===================================================')

# next_sibling를 두번 걸면 다음 p태그로 이동할 수 있다.
print(body.p.next_sibling.next_sibling)
print('===================================================')

for each_tag in soup.find_all('p'):
    print(each_tag.get_text())
print('===================================================')

# get_text()명령으로 태그 안에 있는 텍스트
# 주피터에서 실행시 '/n'도 같이 나오지만 powershell을 진행하기때문에 안나온다.
print(body.get_text())
print('===================================================')

# 클릭이 가능한 링트를 의미하는 'a'
links = soup.find_all('a')
print(links)
print('===================================================')
# a 안에서 클릭 할 수 있는 아이와 클릭링크 가져오기
for each in links:
    href = each['href']
    text = each.string
    print(text + ' -> ' + href)
