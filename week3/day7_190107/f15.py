'''
    STEP1
        디비에서 위에 언급된 데이터를 가져오는 selectTradeDate함수 d7에 구현
    STEP2
        selectTradeData은 모듈 가져오기로 처리
    STEP3
        trade.html 파일을 생성해서 해당 데이터를 출력할 수 있는 html 구성
        컬러명 : 코드 : 이름 : 현재가 : 상한가 : 최저가
    STEP4
        요청하면 해당내용이 작동하여 브라우저에 주식 목록이 나타난다
    STEP5
        검색창을 상단에 붙이고(HTML이용),
        2005년 구글맵에서 많이 이용된 ajax 통신을 이용하여(JS)
            ajax : 화면이 깜빡이지 않고 뒷단(백그라운드)에서 통신을 진행하는 기술
        검색어에 해당되는 종목리스트를 구해서(SQL)
        브라우저로 전송해서(JSON 방식 사용)
        동적으로 화면(DOM)에 뿌린다

title-wrapper > h3 > ytd-badge-supported
'''

from flask import Flask,render_template
from d7 import selectTradeData

app = Flask(__name__)

@app.route('/')
def home():
    # trade를 통해서 html에 쿼리문에서 수행된 데이터 가져옴
    return render_template('trade.html',trades = selectTradeData())

# 이 코드를 메인으로 구동시 서버가동
if __name__ == '__main__':
    app.run(debug=True) 