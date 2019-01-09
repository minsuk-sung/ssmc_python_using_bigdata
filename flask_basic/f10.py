# f8.py 개선
# 로그인시 아이디와 비번이 주소창에 노출되는 부분 개선
# GET, POST방식으로 변경
# /login, /loginProc 는 사실상 하나의 작업이므로 하나의 주소로 /login으로 통합처리
# 이러한 처리방식을 restful 이라 한다
from flask import Flask, request, render_template, redirect, url_for
# request
#   - GET,POST 등 메소드 방식으로 데이터가 전달시 데이터가 들어있는 객체
# render_template
#   - html을 읽어서 랜더링하여 브라우저로 전송하는 텍스트 구성
#   - jinja2라는 템플릿 엔진을 연동 -> 디자이너에게 프로그래밍을 할 수 있게 하자!
#   - jinja2는 html에 변수나 연산등을 넣어서 동적으로 페이지를 구성할 수 있는 엔진
# redirect
#   - 요청을 다른쪽으로 던져주는 역할
# url_for
#   - 함수명을 통해서 라우트된 주소르 반환하는 함수 

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello world!!'

# get방식과 post방식을 모두 허용하는 라우트 정의 
@app.route('/login',methods=['GET','POST'])
def login():

    # GET 방식일 경우
    if request.method == 'GET':
        return render_template('login2.html')

    # POST 방식일 경우 => methods에는 2개밖에 없으므로 else
    else :
        # 1. 아이디 비번을 획득하고
        uid = request.form.get('uid')
        upw = request.form['upw']
        # 1-1 누락된 값이 존재할 경우, 경고 후 되돌린다 
        if not uid or not upw: # 아이디나 비번이 없는 경우
            return render_template('error.html',msg = '비정상적인 접근입니다.')

        # 2. 우리 회원인지 조회하고 ( 차후 DB 조회 )
        print(uid,upw)

        # 3. 회원이면 서비스로 이동
        if uid == 'm' and upw == '1':
            # 3-1. 세션 생성
            # 3-2. 페이지 이동 ( 요청을 포워딩 ) 
            return redirect(url_for('main'))

        # 4. 회원 아니면 경고 후 페이지를 되돌린다
        else :
            return render_template('error.html',msg = '아이디 혹은 비밀번호를 확인해주세요.')

@app.route('/main')
def main():
    return '서비스' 

# 이 코드를 메인으로 구동시 서버가동
if __name__ == '__main__':
    app.run(debug=True) 