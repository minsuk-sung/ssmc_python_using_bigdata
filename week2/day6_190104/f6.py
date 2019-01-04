# 유저(클라이언트)들이 웹페이지를 요청할때 데이터를 보내고 싶으면
# 케이스 => 링크를 클릭, 아이디 비번 넣고 로그인, 댓글 등록 등등
# 방법론 : 웹의 관점에서
#         method 방식(get,post,put...),
#         동적 파라미터 방식 존재
# 여기서는 동적 파라미터를 다룬다    
################################################################
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home(): 
    return 'home page'

# 동적 파라미터 : 주소(URL)안에 데이터를 전달하는 방식
# multi가 id였다고 하면
# 데이터를 보내고자 하는 원 주소 : /users/login하면 
# /users/login/multi
# uid가 동적 파라미터로 전달된다
# 문법 : ~/<파라미터명>
# 매칭함수의 인자에 파라미터명을 넣어서 함수 내부로 전달시킨다 
@app.route('/users/login/<uid>')
def login(uid): 
    return 'login page %s' % uid

# URL 주소 사이에다 동적 파라미터 사용 가능한가? YES
@app.route('/users/login2/<uid>/etc')
def login2(uid): 
    return 'login page %s' % uid

# 정수만 받았으면 좋겠다
# 이 페이지를 진입하려면 정수값을 보내라
# 주소는 ~/cal/sum 이다
# 동적파라미터는 x,y 라는 이름으로 받다서 응답 페이지는  x+y의 값을 보여주는 페이지이다
@app.route('/cal/sum/<int:x>/<int:y>') # 정수만 받기 위해서 int: 을 붙여준다
def sum(x,y):
    return '%s + %s = %s' % (x,y,x+y)

# 동적 파라미터를 여러개 보내는데 가변적으로 하고 싶다!!
@app.route('/cal/sum2/<path:nums>')
def cal(nums):
    # 가변적인 데이터가 전달되었다. 각각 뽑아서 합산하시오
    # 합산이니까 데이터는 숫자로만 넣으시오
    addSum = 0
    data = nums.split('/')
    for i in data:
        addSum += int(i)
    return '합 : %d' % addSum

if __name__ == '__main__':
    app.debug = True
    app.run()