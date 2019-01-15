# 주소 : ~/users/
# app라는 실체가 바뀌면(blueprint)주소의 시작방식이 변경
from service.controller import bp_users as app # app이제 더이상 Flask 객체가 아니라 Blueprint객체
from service.model import db_session
from service.model import dao
from service.model.member import Member

# ~/users/login
# session 없이 갈 수 있는 유일한 페이지라고 가정하자
@app.route('/login')
def login():
    print('로그인',db_session.loginSql('m','1'))
    return 'users home'

# ~/users/logout
@app.route('/logout')
def logout():
    return 'users logout' 

# ~/users/signup
# 회원 가입 : insert 
@app.route('/signup')
def signup():
    # 회원가입
    newUser = Member('minsuk','1234')
    dao.add(newUser)
    dao.commit() # DB에 새로 넣은거니까 업뎃
    return 'users signup'

# 회원 정보 수정 : update
@app.route('/update')
def update():
    # 객체 하나가 user하나랑 대응됨
    user = dao.query(Member).filter_by(uid='multi',upw='1234').first()
    # 비밀번호 변경
    user.pw = '12345'
    dao.commit() # 이걸 해야 반영돼서 변경이 됨
    return 'update'

# 회원 로그인 : select
@app.route('/select')
def select():
    user = dao.query(Member).filter_by(uid='multi',upw='12345').first() # 하나만 가져오기 위해
    if user: # 회원이면 아래와 같은 값이 나온다
        print(user) # <Member 1 multi 1234>
    else: # 회원이 아니면 참고로 None이 나온다
        print(user, '회원 아님')
    return 'select'

# 회원 탈퇴  : delete
@app.route('/delete')
def delete():
    user = dao.query(Member).filter_by(id='3').first() # 하나만 가져오기 위해
    if user:
        print(user)
        # 삭제
        dao.delete(user)
        dao.commit()
    return 'delete'