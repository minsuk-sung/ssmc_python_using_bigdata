################################################################################
# Pooling 방식
from flask_ex.service.model.dbMgr import DBHelper
db_session = None
# 오직 1회만 호출되고, DB 연결도 총 100개의 세션 완성
def initDBHelper(app):
    global db_session
    db_session = DBHelper(app) # helper안에 쿼리를 넣는거

################################################################################
# ORM 방식
# pip3 install sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# 테이블 한개당 클래스 한개와 연결하는 작업
# row 데이터 한개와 class 객체 한개를 연결하는 과정
# 이런 방식을 ORM이라고 한다 => SQL을 하나도 몰라도 DB처리가 가능하다
# 내가 작성한 패턴이나 함수가 sql로 변환돼서 처리됨
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
# Base를 상속받은 클래스가 테이블 하나와 매칭된다 

# DB Session : 향후 DB 사용시 dao만 가져오면 된다
dao = None
# DB Manager
class DBManager:
    # 멤버변수
    __engine = None
    __session = None
    # 정적함수 ( static fuction )
    # app : Flask 객체 
    @staticmethod
    def init(app):
        # DB에 접속 URL 구성
        db_url = 'mysql+pymysql://%s:%s@%s/%s?charset=%s' % (# mysql에 pymysql 연결
            app.config.get('DB_USER'),
            app.config.get('DB_PASSWORD'),
            app.config.get('DB_REAL_URL') 
                if app.config.get('SERVER_RUN_MODE_IS_REAL') 
                else app.config.get('DB_TEST_URL'),
            app.config.get('DB_DATABASE'),
            app.config.get('DB_CHARSET')
        )
        # 엔진 생성
        DBManager.__engine = create_engine(db_url,echo=True)
        # 세션 생성
        DBManager.__session = scoped_session(sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=DBManager.__engine
        ))
        # 글로벌 적용을 통한 다른 곳에서 사용가능하게 처리
        global dao
        dao = DBManager.__session

    @staticmethod
    def init_db():
        from flask_ex.service.model import member
        # 테이블이 없으면 만들어서 처리
        Base.metadata.create_all(bind=DBManager.__engine) # 테이블이 없으면 만들어서 처리해라
