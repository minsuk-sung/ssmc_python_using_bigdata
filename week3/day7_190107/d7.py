# 함수화 처리
# 아이디,비번을 인자로 입력받아서 재활용성을 높이고, 모듈화의 모양새롤 갖추게 됨
#  

import pymysql as pms

def loginSql(uid,upw):
    connection = None
    row = None #  로그인 결과를 담는 변수 
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
                sql =  "select * from users where uid=%s and upw=%s;"
                cursor.execute(sql,(uid,upw))
                row = cursor.fetchone()
                print('%s님 반갑습니다.' % row['name'])
        # # # # # # # # # # # # # # # # # # # # # # # # # # #

    except Exception as e:
        print('Error : ',e)
        # ID/PW Error( Connection X )
        # Query Error
        row = None

    finally:
        if connection:
            # DB Close
            connection.close()
        return row

if __name__ == '__main__':
    loginSql('m','1')