# 주소가 추가 되면 코드가 반복돼서
# 주소가 요청이 오면 처리할 함수를 구성
# 요청 문법
# 브라우저 주소창
# http(프로토콜명) + :// + IP + : + PORT + / + 세부주소 
################################################################
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home(): 
    return 'home page'

# 라우트 : 세부 페이지를 누가 처리할 것인지 함수와 매칭시키는 역할 담당
# 또한 요청을 분석하여 세부 페이지 값을 획득하는 행위
# /users/login 구성하시오
# user에 관련된 모든 페이지는 /users 밑으로 두겠다는 의미 내포
# 이렇게 하나의 사이트(웹사이트/미들웨어)에서 기능별로 URL을 묶고 업무 분담도 가능하게 하는 방식 : Blueprint라 함(고급)
# 일을 기능별로 쪼개고 싶다 할때 쓰는 기법 중 하나임  

@app.route('/users/login')
def login(): 
    return 'login page' 

if __name__ == '__main__':
    app.debug = True
    app.run()