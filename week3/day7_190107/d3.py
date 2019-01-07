# data를 dict으로 받아오기

import pymysql as pms
# # # # # # # # # # # # # # # # # # # # # # # # # # # 
connection = pms.connect(host='localhost',
                             user='root',
                             password='12341234',
                             db='python_db',
                             #port = 3306,
                             charset='utf8')
# # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 1. 커서의 종류를 pms.cursors.DictCursor로 지정
cursor = connection.cursor(pms.cursors.DictCursor)
# {'id': 1, 'uid': 'm', 'upw': '1', 'name': '멀티', 'regdate': datetime.datetime(2019, 1, 7, 14, 14, 23)}
sql = "select *from users where uid='m' and upw='1';"
cursor.execute(sql)
row = cursor.fetchone()
print('%s님 반갑습니다.' % row['name'])
cursor.close()
# # # # # # # # # # # # # # # # # # # # # # # # # # # 

connection.close()