# SQL문에서 동적으로 파라미터 전달하기

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
                                cursorclass = pms.cursors.DictCursor)
    # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    if connection: # 연결이 존재할때만 연결을 닫아라
        with connection.cursor() as cursor:
            # 파라미터를 %s로 대체하자
            # 'm' -> %s로 : 방법1에서는 이렇게
            # sql = "select * from users where uid=%s and upw=%s;" # '' 없애자
            # 1. 전달할 파라미터가 늘어날수록 tuple에 넣어주자
            # cursor.execute(sql,('m','1'))

            # 'm' -> '%s'로 : 방법2에서는 이렇게
            sql = "select * from users where uid='%s' and upw='%s';" % ('m','1')
            # 2. 문자열에서 알아서 해결하기
            cursor.execute(sql)

            print(sql)
            row = cursor.fetchone()
            print('%s님 반갑습니다.' % row['name'])
    # # # # # # # # # # # # # # # # # # # # # # # # # # #

except Exception as e:
    print('Error : ',e)
    # ID/PW Error( Connection X )
    # Query Error

finally:
    if connection:
        # DB Close
        connection.close()