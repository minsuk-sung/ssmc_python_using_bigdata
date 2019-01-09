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

################################################
# 조회하는 쿼리
################################################

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
                order by cur desc
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

# 키워드를 이용하여 해당 이름에 해당 키워드가 포함된 주식 목록을 리턴
def selectStockByKeyword(keyword):
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
                SELECT code, name, cur, high, low 
                FROM tbl_trade
                WHERE name like '%%%s%%';
            ''' % keyword # %를 문자로 인식하게하려면 %%로 해야한다
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

# codd를 이용하여 해당 종목 정보 모두 가져오기
def selectOneStockInfo(code):
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
                SELECT * 
                FROM tbl_trade
                WHERE code = %s;
            '''
            cursor.execute( sql,(code,) )
            # 여러개 데이터를 다 가져올때
            rows    = cursor.fetchone()            
    except Exception as e:
        print('->', e)
        rows = None
    finally:
        if connection:
            connection.close()
    return rows    

################################################
# 수정하는 쿼리
# 코드를 이용하여 cur,rate를 변경한다
# 변경의 성공여부는 영향을 받은 row의 수가 1이상일 경우 해당된다 => 리턴값 
################################################
# stock : dict 라고 하고, key는 column명을 따라간다 
def updateStockInfo(stock):
    connection = None
    result       = None # 수정결과
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
                UPDATE tbl_trade
                SET cur = %s, rate = %s
                WHERE code = %s;
            '''
            cursor.execute( sql,(stock['cur'],stock['rate'],stock['code']) )
            
        # commit 수행 : 실제 디비에 반영시켜라
        # update,delete,insert 다 해당됨
        connection.commit()
        # 영향을 받은 row의 수를 반환해라
        result = connection.affected_rows() 
        

    except Exception as e:
        print('->', e)
        result = 0
    finally:
        if connection:
            connection.close()
    return result


if __name__ == '__main__':
    # print( '=>', loginSql( 'm', '1' ) )
    # rows = selectTradeData()
    # if rows:print( rows)
    # else:   print('데이터가 없다')
    # print('='*100)
    # print(selectStockByKeyword('동화약품'))
    # print(selectOneStockInfo('000020'))
    # key = 'cur'
    # result = 'dd' if key == 'cur' or key =='rate' else 'disable'
    # print(result)
    dic = {
        'cur' : '234234', # 9170
        'rate' : '2343', # 330
        'code' : '000020'
    }
    print('성공' if updateStockInfo(dic) else '실패')