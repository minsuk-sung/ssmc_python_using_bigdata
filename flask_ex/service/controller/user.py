# 주소 : ~/users/
# app라는 실체가 바뀌면(blueprint)주소의 시작방식이 변경
from service.controller import bp_users as app # app이제 더이상 Flask 객체가 아니라 Blueprint객체

# ~/users/login
@app.route('/login')
def home():
    return 'users home'

# ~/users/logout 

# ~/users/signup


