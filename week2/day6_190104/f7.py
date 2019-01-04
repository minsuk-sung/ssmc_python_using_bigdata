# 유저(클라이언트)들이 웹페이지를 요청할때 데이터를 보내고 싶다
# Method 방식
#   GET : 데이터를 헤더(header)에 싣고 전송
#   POST : 데이터는 바디(body)에 싣고 전송
# 요청패킷 = 헤더 + 바디 로 구성된다
# GET방식은 보안에 취약하다
# POST방식은 보안에 좋다 ( GET <-> POST )
# 
# 데이터 추출은 request 객체를 통해서!!
#  
'''
GET의 예시 : 주소 + '?' + 데이터(키=값&키=값&...)

Ex)
https://news.naver.com/main/read.nhn?
oid=018&sid1=102&aid=0004285425&mid=shm&mode=LSD&nh=20190104133020

1. 주소 : https://news.naver.com/main/read.nhn
2. 물음표 : ?
3. 데이터 : oid=018&sid1=102&aid=0004285425&mid=shm&mode=LSD&nh=20190104133020
''' 
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello world'

# ~/test?name=multi
# 이렇게 요청하면 데이터를 받아서 출력하는 라우트 처리하는 함수를 구성하시오
@app.route('/test')
def test():
    # GET 방식으로 데이터 획득하는 방법
    # request.args.get('키') 
    name = request.args.get('name')
    print(name)
    return name

# http://127.0.0.1:5000/login?uid=abc&upw=1234
@app.route('/login')
def login():
    uid = request.args.get('uid')
    upw = request.args.get('upw')
    # print(request.args)
    return 'ID : %s, PW : %s' % (uid,upw)
    #return uid,upw
    
if __name__ == '__main__':  
    app.run(debug=True)