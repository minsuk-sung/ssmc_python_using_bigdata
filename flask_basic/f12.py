# @app -> 데코레이터라고 한다
# 하나의 함수에 여러개의 데코레이터를 연결할 수 있다 
from flask import Flask

app = Flask(__name__)

@app.route('/test/')
@app.route('/test/<uid>') # 동적파라미터가 들어올 경우
def home(uid = None): # 기본값은 None으로 해두자
    if uid:
        return 'uid : %s' % uid
    else:
        return 'test 요청'

# 이 코드를 메인으로 구동시 서버가동
if __name__ == '__main__':
    app.run(debug=True) 

