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

# 주식 종목 리스트 가져오기(코드기준 정렬)
def selectTradeData():
    connection = None
    rows       = None # 주식정보들을 담는 변수
    try:
        connection = pms.connect(host='localhost', # 디비 주소
                            user='root',      # 디비 접속 계정
                            password='12341234', # 디지 접속 비번
                            db='python_db',   # 데이터베이스 이름
                            #port=3306,        # 포트     
                            charset='utf8',
                            cursorclass=pms.cursors.DictCursor) # 커서타입지정
        # 쿼리수행
        with connection.cursor() as cursor:            
            sql    = '''
                select 
                    code, name, cur, high, low 
                from 
                    tbl_trade
                order by code asc
                limit 0, 10;
            '''
            cursor.execute( sql )
            # 여러개 데이터를 다 가져올때
            rows    = cursor.fetchall()            
    except Exception as e:
        print('->', e)
        rows = None
    finally:
        if connection:
            connection.close()
    return rows

if __name__ == '__main__':
    print( '=>', loginSql( 'm', '1' ) )
    rows = selectTradeData()
    if rows:print( rows)
    else:   print('데이터가 없다')