# 요구사항
# /login, /logout 이라는 페이지를 추가 주문
# 응답 내용은 알아서
# home : http://127.0.0.1:5000/
# login : http://127.0.0.1:5000/login
# logout : http://127.0.0.1:5000/logout  

from flask import Flask

app = Flask(__name__)

@app.route('/') # 패턴
def home(): # 주소함수
    return 'home page'

@app.route('/login')
def login():
    return 'login page'

@app.route('/logout')
def logout():
    return 'logout page'

# 이 코드를 메인으로 구동시 서버가동
if __name__ == '__main__':
    app.run(debug=True) 