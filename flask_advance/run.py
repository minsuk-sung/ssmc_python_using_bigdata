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

from flask import Flask,render_template,url_for,request,redirect,session,json,jsonify
from db.sql import *

app = Flask(__name__)
app.secret_key = 'aslkdfjklsdsdflkjs'

# 세션 생성, 해체, 체크

########################################################

config = {
    'site_title' : '점심 메뉴 분석',
    'menu1' : '오늘의 코스닥 지수 : 150',
    'login' : '로그인'
}

########################################################

@app.route('/')
def home():
    #print('home')
    # 세션이 없으면 로그인으로
    if not 'user_id' in session:
        return redirect(url_for('login'))
    return render_template('index.html',config=config)

########################################################

@app.route('/logout')
def logout():
    # 세션 제거
    if 'user_id' in session:
        session.pop('user_id',None) # del session['user_id'] 라고 해도 됨
    if 'user_nm' in session:
        session.pop('user_nm',None)

    # 홈페이지 이동 
    # return render_template('logout.html',config=config)
    return redirect(url_for('login'))

########################################################

# restful 방식
# get방식과 post방식을 모두 허용하는 라우트 정의  
@app.route('/login',methods=['GET','POST'])
def login():

    # GET 방식
    if request.method == 'GET':
        return render_template('login.html',config=config)

    # POST 방식
    else :
        uid = request.form['uid']
        upw = request.form['upw']
        row = loginSql(uid,upw)
        print( row, uid, upw )
        if row:
            # 세션 생성
            #   클라이언트 정보를 서버가 유지하거나 보관
            #   단, 서버가 들고 있으면 리소스가 부족해지거나 성능 저하를 가져올 수 있다
            #   실습할때는 서버 메모리에 들고 있을 것이고, 서비스할때는 디비나 서드파트 솔루션 이용하여 처리
            session['user_id'] = uid
            session['user_nm'] = row['name']

            # 홈페이지 이동 
            return redirect(url_for('home'))
        else :
            return render_template('error.html',msg = '아이디 혹은 비밀번호를 확인해주세요.')

########################################################

@app.route('/tradeList')
def tradeList():
    return render_template('sub/tradeList.html',config=config,
                                                trades = selectTradeData())

########################################################

@app.route('/search',methods=['POST'])
def search():
    # 검색어 획득
    keyword = request.form['keyword']
    # 검색 쿼리 수행
    rows = selectStockByKeyword(keyword)
    #print(rows)

    # 검색 결과가 있으면(성공) json 형식으로 응답
    if rows:
        return jsonify(rows)

    # 검색 결과가 없으면(실패) json의 다른 형태로 응답
    else:
        return jsonify([])

########################################################

# 이 코드를 메인으로 구동시 서버가동
if __name__ == '__main__':
    app.run(debug=True) 