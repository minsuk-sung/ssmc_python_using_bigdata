# f7.py 업그레이드 버전
# 실제 로그인은 로그인 페이지에서 아이디 비번을 넣고
# 로그인을 눌렀을때 작동
# 로그인 화면을 만들어주는 html의 이해와 이를 처리하는 방법을 알아야함
# 
# 브라우저에서 클라이언트 화면을 구성하는 3요소
#   1. HTML5 (25%)
#       웹화면을 구성하는 콘텐츠를 가지고 있다. 구조를 가지고 있다. 뼈대,콘텐츠 ...
#   2. CSS3 (25%)
#       레이아웃을 담당하고 프리젠테이션,데코레이션,디자인,애니메이션 등을 담당
#       이게 없으면 화면은 보잘것 없어짐
#       여기까지만 하면 정적 페이지 
#   3. JavaScript (50%)
#       오퍼레이션 담당, 인터렉션(사용자와 주고받기)
#       이벤트처리( 통신처리(ajax), 동적페이지(DHTML,DOM) 구성 )
#       이걸 중심으로 웹페이지를 만드는 기술들
#           - Angular js (구글)
#           - React js (페이스북)
#           - Vue (개발자 커뮤니티)
#       JavaScript Framework => JQuery 생산성이 향상됨
#         
# 
# 1~3번을 관장하는 기관 : W3C
# 
# JS도 NodeJS하고 좀 다르다 언어는 같은데
# NodeJS는 웹서버쪽 
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    # html의 태그들로 표현을 하면 브라우저는 파싱을 통해
    # 한줄한줄 해석하면서 화면을 그려나간다
    # 그러면서 <...>태그로 구성된 부분은 화면에 그리지 않고
    # 해당 태그의 의미에 맞춰서 화면 처리를 한다
    # <h2> : 해드라인 태그 h1~h4
    # 숫자가 작아질수록 커진다.  
    return '<h2>hello world</h2>'

@app.route('/login')
def login():
    # html파일을 찾아서 읽어서 텍스트로 변환
    return render_template('login.html') # import에서 render_template를 했기 때문에

# DB가 없는 관계로
# 회원은 아이디가 m이고 비번은 1이라고 하자 
@app.route('/loginProc')
def loginProc():
    uid = request.args.get('uid')
    upw = request.args.get('upw')
    # upw = request.args.get['upw'] #이렇게도 가능하다
    # 회원이면 =>  반갑습니다 m님
    if uid == 'm' and upw == '1':
        # return '환영합니다 %s님' % uid
        # 요청에 대해서 바로 응답하지 않고 다른 페이지로 요청을 던진다
        # 세션 생성 => 로그인 햇음을 인지하는 방법, 사용자 정보를 저장하는 용도  
        return redirect('/main') # 리다이렉팅( redirecting )
    # 회원이 아니면 => 아이디 혹은 비밀번호를 확인해주세요
    else: 
        return '''
        <script>
            alert('아이디 혹은 비밀번호를 확인해주세요');
            history.back();
        </script>
        '''
        # 위의 코드는 자바스크립트
        # history.back() 은 방문기록을 뒤로 가게 하는 함수 
    #return uid,upw

# 메인 서비스 화면 ~/main
# 화면 내용은 그냥 서비스 
@app.route('/main')
def main():
    # 로그인을 해야지만 진입할 수 있는 페이지
    # 로그인 여부를 판단할 수 있어야 필터가능 => 세션(session)
    #  
    return '서비스' 


if __name__ == '__main__': # 이 코드를 메인으로 구동시 서버가동
    app.run(debug=True)