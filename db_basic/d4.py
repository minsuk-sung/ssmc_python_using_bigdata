# data를 dict으로 받아오기 -> 최초 접속시 처리

import pymysql as pms
# # # # # # # # # # # # # # # # # # # # # # # # # # # 
connection = pms.connect(host='localhost',
                             user='root',
                             password='12341234',
                             db='python_db',
                             #port = 3306,
                             charset='utf8',
                             cursorclass = pms.cursors.DictCursor) # cursor type 지정
# # # # # # # # # # # # # # # # # # # # # # # # # # # 
cursor = connection.cursor()
sql = "select *from users where uid='m' and upw='1';"
cursor.execute(sql)
row = cursor.fetchone()
print('%s님 반갑습니다.' % row['name'])
cursor.close()
# # # # # # # # # # # # # # # # # # # # # # # # # # # 

connection.close()