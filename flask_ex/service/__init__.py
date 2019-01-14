from flask import Flask

def create_app(config_path = './resource/config.cfg'):
    app = Flask(__name__)
    # 각종 설정 삽입될것
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # 1. 환경변수 설정
    initConfig(app,config_path)
    # 2. DB 설정
    #   - 
    #   
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # 
    # 3. Error 설정
    #   - 
    #  
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # 
    # 4. 라우트 설정( 블루프린트 )
    #   - blueprint => 주제별로 페이지를 나눠서 개발가능 => controller
    #       - 회원관리 : ~/users/login, ~/users/logout, ~/users/signup
    from service.controller import bp_users,bp_analysis
    #       - 분석관리 : ~/analysis/init, ~/analysis/proc, ~/analysis/sum    
    from service.controller import user,ana # 해당 모듈이 통째로 메모리에 올라온다 -> 객체가 만들어지듯이 사용에 관계없음
    # blueprint를 Flask 객체에 등록
    # http://127.0.0.1:3000/users/login 로 접속해야함
    app.register_blueprint(bp_users, url_prefix='/users')
       
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    # 
    # 5. LifeCycle 처리
    #   - 
    #  
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
    return app

def initConfig(app,config_path):
    # 1. 환경변수 설정
    #   - 프로그램에서 사용되는 고정된 정보
    #   - 디비접속정보, 운영상 필요한 상수값 등
    #   - class로부터(객체),리소스(파일),운영체제로부터 가져올 수 있다
    #   - 코드에 하드코딩되어있지 않고, 환경변수를 읽어서 프로그램에 반영시키는 방식 => 관리나 유지보수가 좋다     
    app.config.from_pyfile( config_path, silent=True ) # cfg 파일을 읽기 위해

    # class를 읽어서 객체로부터 환경변수를 획득 
    # -> 직관성, 코드에 적용되어 있음
    # 내 위치가 하위에 있다고 하더라도 from을 기술할때는 풀경로를 기술 
    from service.config import DBConfig # 시작은 start.py이니까
    app.config.from_object( DBConfig )

    # 로그된 환경변수값 확인
    # configCheck(app.config.items())
    # TEST_URL에 해당된는 값을 출력하시오
    # 환경변수의 값은 그 의도대로 타입을 따라간다 
    print(app.config['DB_PORT'])
    # print(app.config.get('TEST_URL'))
    # print(app.config.get('SERVER_RUN_MODE_IS_REAL'))

def configCheck(items):
    # print(items)
    # 환경변수 키, 환경변수 값 출력 <- dict 형태니까
    for key,value in items:
        print(key,value)