import sqlite3
sqlite3.sqlite_version
conn = sqlite3.connect(':memory:')          #메모리 DB접속(일회성)
conn = sqlite3.connect('.test.db')          #파일 DB접속(일회성)
'''
데이터 쿼리 수행
'''
conn.commit() #변경사항 저장
conn.close()
