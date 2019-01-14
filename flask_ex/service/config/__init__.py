# 환경변수를 클래스로 정의
# 방법은 멤버변수로 지정하면 됨
# DB 접속주소만 다르게 하고 나머지는 모두 동일하게 테스트(개발),상용 의 정보를 동일하게 설정  
class DBConfig(object):
    '''
    멤버변수
    '''
    DB_TEST_URL   = '127.0.0.1' # DB TEST IP
    DB_REAL_URL   = '' # DB REAL IP
    DB_PORT       = 3306 # DB PORT
    DB_USER       = 'root' # 사용자 계정 - 원래는 root를 사용하면 안됨
    DB_PASSWORD   = '12341234' # 사용자 비번
    DB_DATABASE   = 'python_db' # database 명
    DB_CHARSET    = 'utf8' # 문자셋
    MAX_POOL      = 100 # 디비 커넥션 최대수 ( 만약 풀링기법을 사용하려면 )
    