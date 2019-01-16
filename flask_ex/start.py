from flask_ex.service import create_app # service 폴더 안에 __init__.py로 실행됨

# create_app가 Flask 객체를 리턴
app = create_app()

# 서버 가동
if __name__ == '__main__':
    host = None
    port = None

    # 외부 변수를 이용해서 프로그램을 컨트롤하고자 함
    # 실제 환경
    if app.config.get('SERVER_RUN_MODE_IS_REAL'): 
        host = app.config.get('REAL_URL')
        port = app.config.get('REAL_PORT')
    # 테스트 환경    
    else :
        host = app.config.get('TEST_URL')
        port = app.config.get('TEST_PORT')

    app.run(
        host = host,
        port = port,
        debug = app.config.get('SERVER_RUN_MODE_IS_DEBUG') )