# 주소 뒤에 /를 붙이는 여부
# ~/pro
# !/pro/
# 이 2개의 주소를 같은것으로 볼 것인가? 
from flask import Flask

app = Flask(__name__)

# ~/pro/ : 404 Not Found (존재하지 않는 페이지)
@app.route('/pro')
def home():
    return 'hello world!'

# ~/pros/, ~/pros 둘다 허용하게
@app.route('/pro2/') # 마지막에 /를 붙여주자
def pro2():
    return 'hello world!!'

# 이 코드를 메인으로 구동시 서버가동
if __name__ == '__main__':
    app.run(debug=True) 

