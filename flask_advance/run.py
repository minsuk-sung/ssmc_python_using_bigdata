# ./templates : html 파일들이 위치하는 곳
# ./static   : 리소스 파일들이 위치하는 곳(js,css,img ...)
#       static 밑에 있는 모든 리소스는
#       http://localhost/static/리소스명 이렇게 직접 접근 가능
#       즉, 라우팅 할 필요가 없다 무조건 웹경로로 인식한다 
'''
    1. 이미 작성된 템플릿 익히기
        - SB Admin에서 다운로드 : https://github.com/BlackrockDigital/startbootstrap-sb-admin-2/archive/gh-pages.zip
        - static : 라우팅 안해도 그냥 접근가능
    2. 템플릿 쪼개서 조합하기
    3. 파일 업로드 
    4. 세션,쿠키 처리 ( 로그인 업그레이드 )
'''  

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# 이 코드를 메인으로 구동시 서버가동
if __name__ == '__main__':
    app.run(debug=True) 