# dbms_mysql.py

import pymysql

# MySQL 서버에 연결하는 함수
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="123663",
    database="exampledb",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)

# 커서 생성 => 커서 통해서 명령어 작성
cursor = conn.cursor()

# 명령어 실행
cursor.execute("SELECT DATABASE()")
# 한번 호출에 하나의 Row를 가져올 때 사용
print("현재 데이터베이스: ", cursor.fetchone())     # 하나의 데이터 가져오기
# print("현재 데이터베이스: ", cursor.fetchall())   # 모든 데이터 가져오기
# print("현재 데이터베이스: ", cursor.fetchmany(2)) # 여러개 데이터 가져오기

# 연결 해제 함수
conn.close()


