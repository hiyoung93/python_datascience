# -------------------- 메모리 DB 접속하기(일회성)
import sqlite3
con = sqlite3.connect(':memory:')

# -------------------- 파일 DB 접속하기
import sqlite3
con = sqlite3.connect('./test.db')

'''
특수이름 :memory: 제공해서 램에 db 생성가능

connection 얻으면 cursor객체 만들고 execute() 호출해서 SQL명령수행가능
'''
# --------------------------------------------- 데이블 생성

cur = con.cursor()
cur.execute("CREATE TABLE PhoneBook(Name text, PhoneNum text);")

# --------------------------------------------- 데이터 삽입
 ''' 기본 strinf query 사용'''
cur = con.cursor()
cur.execute("INSERT INTO PhoneBook Value('Derick', '010-1234-4511');")

'''parameter: Tuple 사용'''
name = 'hiyoung'
phoneNumber = '010-1234-4511'
cur = con.cursor()
cur.execute('INSERT INTO PhoneBook VALUES(?, ?);',(name, phoneNumber))

'''Named parameter: Dictionary 사용'''
name = 'hiyoung'
phoneNumber = '010-1234-4511'
cur = con.cursor()
cur.execute('INSERT INTO PhoneBook VALUES(:name, :phoneNumber);',
            {'name':name, 'phoneNumber':phoneNumber})
'''list 사용'''
dataList = (('Tom', '010-1234-4511'),('DSP','010-1234-4511'))
cur = con.cursor()
cur.executemany('INSERT INTO PhoneBook VALUES(?, ?);', dataList)


# -------------------------------------------- 데이터 조회
# -------------------- 순회 조회
cur.execute('SELECT * FROM PhoneBook')
for row in cur:
    print(row)
# -------------------- 단건 조회
cur.execute('SELECT * FROM PhoneBook')
print(cur.fetchone())
# -------------------- 다건 조회
cur.fetchmany(2)
# -------------------- 모두 조회
cur.fetchall()
