# 템플릿 엔진에서 값 찍기
# 전달 : render_template('abc.html', 키=값,키=값 ...) 
# 받는 쪽(html) : 값 출력 => {{ 키 }} 
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    data = [
        {'rank':1, 'nation':'Korea'},
        {'rank':2, 'nation':'US'},
        {'rank':3, 'nation':'Japan'}
    ]
    return render_template('index.html', items = data)

# 이 코드를 메인으로 구동시 서버가동
if __name__ == '__main__':
    app.run(debug=True) 