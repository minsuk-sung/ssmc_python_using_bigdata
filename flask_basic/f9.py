# Flask 내에서 구성하는 모든 페이지 내에 주소를 참조하거나
# 사용시 직접적으로 주소(URL)를 기입하지 않는다
# redirecting('/main') => X
# => url_for('기술하고자 하는 주소와 라우팅 된 함수명') 함수를 사용
# 일단 주소,동적파라미터 스타일, 리소스(css,js,img 등 참조) 주소 등의 형태가 존재
from flask import Flask, url_for, redirect

app = Flask(__name__)

# 홈페이지
@app.route('/')
def home():
    # 홈페이지를 진입하면 바로 메인페이지로 이동
    # 함수명을 통해 연결된 주소를 획득한다 -> 함수명은 고유할테니까
    return redirect(url_for('main'))

# 메인 페이지
# 주소가 변경돼도 함수명으로 참조되었기 때문에 유지보수 측면에서는
# 최소의 수정만으로 발생되고, 전체적으로 운영에는 지장없다 
@app.route('/hahahah') # 여기가 꼭 '/main'일 필요가 없음 => url_for가 알아서 가져옴
def main():
    # 로그인을 해야지만 진입할 수 있는 페이지
    # 로그인 여부를 판단할 수 있어야 필터가능 => 세션(session)
    return '서비스2' 

# 이 코드를 메인으로 구동시 서버가동
if __name__ == '__main__':
    app.run(debug=True) 