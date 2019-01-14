# 주소 : ~/users/
# app라는 실체가 바뀌면(blueprint)주소의 시작방식이 변경
from service.controller import bp_users as app # app이제 더이상 Flask 객체가 아니라 Blueprint객체

# ~/users/login
# session 없이 갈 수 있는 유일한 페이지라고 가정하자
@app.route('/login')
def login():
    return 'users home'

# ~/users/logout
@app.route('/logout')
def logout():
    return 'users logout' 

# ~/users/signup
@app.route('/signup')
def singup():
    return 'users signup'

