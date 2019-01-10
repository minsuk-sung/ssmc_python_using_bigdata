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

from flask import Flask,render_template,request,json, jsonify
# from d7 import selectTradeData,selectStockByKeyword,selectStockByCode
from d7 import *

app = Flask(__name__)

@app.route('/')
def home():
    # trade를 통해서 html에 쿼리문에서 수행된 데이터 가져옴
    return render_template('trade.html',trades = selectTradeData())

# 검색
@app.route('/search',methods=['POST'])
def search():
    # 검색어 획득
    keyword = request.form['keyword']
    # 검색 쿼리 수행
    rows = selectStockByKeyword(keyword)
    #print(rows)

    # 검색 결과가 있으면(성공) json 형식으로 응답
    if rows:
        return jsonify(rows)

    # 검색 결과가 없으면(실패) json의 다른 형태로 응답
    else:
        return jsonify([])

# 코드별 상세 페이지
@app.route('/info/<code>') # 동적 파라미터
def info(code):
    '''
        # code값이 없으면 back => 동적 파라미터 특성상 값이 없으면 404 Error
        # if not code:
        #     return render_template('error.html',msg = '정보누락')
        ##########################################################
        # code값이 있으면 코드를 기준으로 종목정보 전체를 획득
        #   종목 정보를 화면에 표시
        # ---------------------- 
        #   컬럼        :   값
        # ---------------------- 
        #   왼쪽에 컬럼명 : 오른쪽에 값
        # ----------------------
    '''  
    print('업데이트 여부',request.args.get('update')) # 콘솔창에 업데이트 여부가 뜸
    return render_template('info.html', trade = selectOneStockInfo(code),
                                        update = request.args.get('update'))

# 종목 정보 수정하기
@app.route('/updateStock',methods=['POST'])
def updateStock():
    # 1. 파라미터 획득
    # print(request.form) # ImutableMultiDict([('cur','1')('rate','10')]) <- list,tuple...dict이 아님
    # 2. 쿼리 수행

    # 3. 수행 결과 판단
    #   수정이 성공하면 -> /info/code 화면으로
    if updateStockInfo(request.form):
        return render_template('error.html',msg='수정완료',
                                            url='/info/' + request.form['code'])
    #   수정이 실패하면 -> 경고창 띄우고 되돌아가기
    else:
        return render_template('error.html',msg='수정실패')
    # return "%s"  % updateStockInfo(request.form)
    

# 이 코드를 메인으로 구동시 서버가동
if __name__ == '__main__':
    app.run(debug=True) 