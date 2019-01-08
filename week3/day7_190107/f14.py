# f10에서 로그인을 연결한 쿼리 
from flask import Flask, request, render_template, redirect, url_for
from d7 import loginSql


app = Flask(__name__)

@app.route('/')
def home():
    return 'hello world!!'

@app.route('/login',methods=['GET','POST'])
def login():

    if request.method == 'GET':
        return render_template('login2.html')

    else :
        uid = request.form.get('uid')
        upw = request.form['upw']

        if not uid or not upw:
            return render_template('error.html',msg = '비정상적인 접근입니다.')

        print(uid,upw)

        if loginSql(uid,upw): # uid == 'm' and upw == '1':
            return redirect(url_for('main'))

        else :
            return render_template('error.html',msg = '아이디 혹은 비밀번호를 확인해주세요.')

@app.route('/main')
def main():
    return '서비스2' 

if __name__ == '__main__':
    app.run(debug=True) 