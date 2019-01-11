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
import os

app = Flask(__name__)
app.secret_key = 'aslkdfjklsdsdflkjs'

# 세션 생성, 해체, 체크

########################################################

config = {
    'site_title' : 'MS Stock Site',
    'menu1' : 'Check or Search Stock',
    'menu2' : 'File Upload',
    'login' : 'Login'
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
        # print( row, uid, upw )
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

@app.route('/uploadPhoto',methods=['GET','POST'])
def uploadPhoto():
    if request.method == 'GET':
        rows = selectFileData() # GET으로 하는구나...
        return render_template('sub/uploadPhoto.html',
                                config=config,
                                items=rows)
    else :
        # 딕셔너리 구조로
        # 디비에 들어갈 데이터를 준비
        dic = dict() 

        # 1. 전달된 데이터를 콘솔에 출력한다 ( 작성자 아이디 포함 )
        print(request.form['title'])
        print(request.form['content'])
        print(session['user_id'])
        
        # 2. File 저장처리
        # 파일 1개를 보냈을때 
        # f = request.files['fileData']
        # print(type(f),f)
        # 파일 여러개를 보낼 경우 
        tmp = list()
        for f in request.files.getlist('fileData'): 
            print(type(f),f, f.filename)
            # 윈도우,리눅스 어떤 경로든 알아서 적용되게 구현해야한다
            # 어디에 저장할 것인가? 정적 url을 제공하는 위치
            # ~/static/upload
            # 사용자별로 구분 -> 아이디를 폴더로 or 파일명에 아이디를 붙이기
            # 동일파일 구분 -> 시간을 추가
            # 궁극적인 해결방안 -> 중복되지 않는 해시값(16-32바이트)으로 이름변경 
            # path = os.getcwd() + '/static/upload/' + f.filename
            path = os.path.join( os.getcwd(),'static','upload',f.filename )
            print(path) 
            f.save(path)
            # 파일명추가
            tmp.append(f.filename)

            # 디스크상 저장 위치
            # /Users/minsuksung/github/ssmc_python_using_bigdata/flask_advance
            # 웹경로상
            # http://127.0.0.1:5000/static/upload/가니메데스.jpg
            # 저장위치는 무조건 http://127.0.0.1:5000/ 고정
            # 그렇다면 저장은 파일명만
            # a.jpg | b.jpg | c.jpg ... 
           
            # 디비에 입력된 파일 정보를 출력
            # 어떤 정보만 디비에 들어가면 되는지 고민해서 출력
        
        dic['title'] = request.form['title']
        dic['content'] = request.form['content']
        dic['author'] = session['user_id']
        dic['files'] = '|'.join(tmp)
        print(dic)

        # 3. DB 입력처리
        result = insertFileData( dic )
        # 성공하면 저장되었다고 -> 리스트로 이동
        if result:
            return render_template('error.html',
                                    msg='등록성공',
                                    url=url_for('uploadPhoto'))
        # 실패하면 실패되었다고하고 돌아가기
        else :
            return render_template('error.html',msg='등록실패')
        # return "%d개의 파일 업로드 처리" % result
        

########################################################

# 이 코드를 메인으로 구동시 서버가동
if __name__ == '__main__':
    app.run(debug=True) 