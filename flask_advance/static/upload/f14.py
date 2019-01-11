# f10 버전에 로그인 쿼리를 연결한 버전
from flask import Flask, request, render_template, redirect, url_for
from d7 import loginSql

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello world3'

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login2.html')
    else:
        uid = request.form.get('uid')
        upw = request.form['upw']
        if not uid or not upw:
            return render_template('error.html', msg='비정상접근')
        if loginSql( uid, upw):#uid == 'm' and upw == '1':            
            return redirect( url_for('main') )
        else:            
            return render_template('error.html', msg='아이디비번 확인요청')

@app.route('/main')
def main():
    return "서비스"

if __name__=='__main__':
    app.run(debug=True)