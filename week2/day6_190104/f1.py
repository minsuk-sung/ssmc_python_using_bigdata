# 가장 최소로 구성된 웹서비스 구성

# 1. flask 모듈 가져오기
from flask import Flask

# 2. Flask 객체 생성
app = Flask(__name__)

# 3. 브라우저에서 사용자가 특정 페이지를 보기 위해서 
# 규약에 맞게 주소창에 주소를 치고 엔터를 치면 서버로 요청이 들어온다
# 요청이 들어오면 라우트는 분석해서 주소는 누가 처리할지 오더를 내린다 : 라우팅 수행
# '/' : 홈페이지, 기본 주소나 도메인만 작성한 형태
# @ : decoration  
@app.route('/')
def home():
    return 'hello world3'

# 4. 서버 가동 == 프로그램 가동
app.run(debug=True) # 디버깅 모드 : 새로고침만 하면 바로바로 바뀐거 볼 수 있게

