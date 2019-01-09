# with문을 사용하여 close 처리하기
# try문을 통해 비정상 종료를 없애고 
# 정상적인 처리 부분을 완성 

import pymysql as pms

connection = None
try:
    # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    connection = pms.connect(host='localhost',
                                user='root',
                                password='12341234',
                                db='python_db',
                                #port = 3306,
                                charset='utf8',
                                cursorclass = pms.cursors.DictCursor) # cursor type 지정
    # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    if connection: # 연결이 존재할때만 연결을 닫아라
        with connection.cursor() as cursor:
            sql = "select *from users where uid='m' and upw='1';"
            cursor.execute(sql)
            row = cursor.fetchone()
            print('%s님 반갑습니다.' % row['name'])
    # # # # # # # # # # # # # # # # # # # # # # # # # # #

except Exception as e:
    print('Error : ',e)
    # ID/PW Error( Connection X )
    # Query Error

finally:
    if connection: # 있을때만 닫자
        # DB Close
        connection.close()