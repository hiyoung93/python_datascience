from bs4 import BeautifulSoup
from urllib.request import urlopen

url_base = 'http://www.chicagomag.com'
url_sub = '/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/'
url = url_base + url_sub

html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')


print(soup.find_all('div','sammy'))
