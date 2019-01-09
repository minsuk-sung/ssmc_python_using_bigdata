import pymysql as sql

# 1. DB Open
# Connect to the database
connection = sql.connect(host='localhost',
                             user='root',
                             password='12341234',
                             db='python_db',
                             #port = 3306,
                             charset='utf8')

# print('DB OPEN')

# 2. Query Execute
# 2-1. Cursor 획득
cursor = connection.cursor()
# 2-2. SQL 준비
sql = "select *from users where uid='m' and upw='1';" # 홀따옴표 조심
# 2-3. Query 수행
cursor.execute(sql)
# 2-4. 결과 획득 : rows 획득, 결과 집합 획득
row = cursor.fetchone() # tuple로 가져오는듯
# print(row)
print('%s님 반갑습니다.' % row[3]) # 순서를 기반으로 획득하면 구조 변경시 자동 대응이 안된다
# 데이터가 dict으로 처리하여 문제를 해결하자
# 2-5. Cursor 닫기
cursor.close()

# 3. DB Close
connection.close()
# print('DB CLOSED')