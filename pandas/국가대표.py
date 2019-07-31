
# -------------------- 데이터베이스 접속하기
import sqlite3

conn = sqlite3.connect(':memory:') # 메모리 DB접속(일회성)
conn = sqlite3.connect('./test.db') # 파일 DB접속(일회성)
'''
데이터 쿼리 수행
'''
conn.commit() # 변경사항 저장
conn.close()

# -------------- with 문 이용
conn = sqlite3.connect('./test.db')

with conn:
    cur = conn.cursor()
    cur.execute('SELECT * FROM test_table')
    rows = cur.fetchall()
    for row in rows :
        print(row)
