'''
    - 파이썬에서 DB 접속 및 해제
    - Query 수행 => 여기서는 ORM 방식 사용
        -> row 방식
            - 매번 접속, 해제를 하기 때문에 풀링(polling) 사용으로 속도나 성능을 해결해야함
            - pip install DBUtils
            - 풀링(polling)
            : 특정 수만큼 DB와 연결을 맺어서 보관하고 있고 요청이 들어오면 빌려주고 사용이 끝나면 반납
        -> ORM 방식 : 
    
'''
import pymysql as my
from DBUtils.PooledDB import PooledDB

class DBHelper:
    '''
    멤버변수
    '''
    # DB 연결 정보
    app = None
    # 풀링 객체(DB와 연결정보를 가지고있는 객체)
    connectionPool = None

    ##################################################
    # 생성자
    def __init__(self,app):
        self.app = app
        self.initPool() # 객체가 생성되면 바로 DB가 붙어서
    # 소멸자
    def __del__(self):
        self.freePool()
    ##################################################
    # Connection Pool 생성
    def initPool(self):
        # 아래 코드 수행 후 connectionPool 객체는 총 100개(maxconnections 수)
        # 디비와 연결 세션을 가지고 있게 된다 
        self.connectionPool = PooledDB(
            creator = my,
            # 값1 if 조건문 else 값2
            host = self.app.config.get('DB_REAL_URL') 
                if self.app.config.get('SERVER_RUN_MODE_IS_REAL') 
                else self.app.config.get('DB_TEST_URL'),
            user = self.app.config.get('DB_USER'),
            password = self.app.config.get('DB_PASSWORD'),
            database = self.app.config.get('DB_DATABASE'),
            charset = self.app.config.get('DB_CHARSET'),
            maxconnections = self.app.config.get('MAX_POOL'),

            autocommit = False,
            blocking = False,
            cursorclass = my.cursors.DictCursor
        )
    # Connection Pool 소멸
    def freePool(self):
        # 잡아두고 있던 100개의 디비 세션을 모두 반납한다
        if self.connectionPool: # 존재한다면
            self.connectionPool.close()
    ##################################################
    # Login
    def loginSql(self,uid,upw):
        row = None #  로그인 결과를 담는 변수 
        connection = None
        try:
            # DB 연결 세션 하나 빌림
            connection = self.connectionPool.connection()
            # # # # # # # # # # # # # # # # # # # # # # # # # # # 
            with connection.cursor() as cursor:
                sql =  "select * from users where uid=%s and upw=%s;"
                cursor.execute(sql,(uid,upw))
                row = cursor.fetchone()
                # print('%s님 반갑습니다.' % row['name'])
            # # # # # # # # # # # # # # # # # # # # # # # # # # #

        except Exception as e:
            print('Error : ',e)
            # ID/PW Error( Connection X )
            # Query Error
            row = None

        finally:
            if connection:
                connection.close()
        return row
