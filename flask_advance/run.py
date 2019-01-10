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

from flask import Flask,render_template,url_for,request,redirect

app = Flask(__name__)

config = {
    'site_title' : '점심 메뉴 분석',
    'menu1' : '오늘의 코스닥 지수 : 150',
    'login' : '로그인'
}

@app.route('/')
def home():
    return render_template('index.html',config=config)

@app.route('/logout')
def logout():
    # 세션 제거
    # 홈페이지 이동 
    return render_template('logout.html',config=config)

# restful 방식
# get방식과 post방식을 모두 허용하는 라우트 정의  
@app.route('/login',methods=['GET','POST'])
def login():

    # GET 방식일 경우
    if request.method == 'GET':
        return render_template('login.html',config=config)

    # # POST 방식일 경우 => methods에는 2개밖에 없으므로 else
    # else :
    #     # 1. 아이디 비번을 획득하고
    #     uid = request.form.get('uid')
    #     upw = request.form['upw']
    #     # 1-1 누락된 값이 존재할 경우, 경고 후 되돌린다 
    #     if not uid or not upw: # 아이디나 비번이 없는 경우
    #         return render_template('error.html',msg = '비정상적인 접근입니다.')

    #     # 2. 우리 회원인지 조회하고 ( 차후 DB 조회 )
    #     print(uid,upw)

    #     # 3. 회원이면 서비스로 이동
    #     if uid == 'm' and upw == '1':
    #         # 3-1. 세션 생성
    #         # 3-2. 페이지 이동 ( 요청을 포워딩 ) 
    #         return redirect(url_for('main'))

    #     # 4. 회원 아니면 경고 후 페이지를 되돌린다
    #     else :
    #         return render_template('error.html',msg = '아이디 혹은 비밀번호를 확인해주세요.')

# 이 코드를 메인으로 구동시 서버가동
if __name__ == '__main__':
    app.run(debug=True) 