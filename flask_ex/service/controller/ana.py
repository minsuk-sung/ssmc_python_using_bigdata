# 주소 : ~/ana/
# app라는 실체가 바뀌면(blueprint)주소의 시작방식이 변경
from service.controller import bp_analysis as app # app이제 더이상 Flask 객체가 아니라 Blueprint객체

# ~/analysis/init
@app.route('/init')
def init():
    return 'users init'

# ~/analysis/proc
@app.route('/proc')
def proc():
    return 'users proc' 

# ~/analysis/sum
@app.route('/sum')
def sum():
    return 'users sum'

