'''

MySQL 설명서

brew 설치
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

설치
brew install mysql@8.0

구동
mysql.server start

root 비번
mysql_secure_installation -> no -> 비번입력 -> y -> y -> n -> y

로그인 확인 
mysql -uroot -p
비번입력

기본포트 : 3306

클라이언트툴
https://www.sequelpro.com/

비번바꿀때
alter user 'root'@'localhost' identified with mysql_native_password by '12341234';

Python에서 MySQL 접금 및 쿼리 수행
Flask 자체 모듈도 있지만, MySQL 전용 담당 모듈도 존재한다
여기서는 PyMySQL 사용!
pip install pymysql

-- 로그인 쿼리 ->회원인지 아닌지 체크 그리고
-- 회원이면 회원 데이터도 같이 보내는(추가)
-- *는 모든 컬럼을 다 가져오는 행위이므로
-- 데이터가 많고 컬럼이 많으면 성능저하 원인
-- 실제는 필요한것만 가져온다
-- 조회
select *from users;
-- 특정 아이디와 특정 비번에 해당 되는 row 데이터
-- 조건을 부여해라!!
select *from users where uid='m' and upw='1';

'''
# PyMySQL 모듈 가져오기
import pymysql as sql

# DB Open
# Connect to the database
connection = sql.connect(host='localhost',
                             user='root',
                             password='12341234',
                             db='python_db',
                             #port = 3306,
                             charset='utf8')

print('DB OPEN')

# Query Execute

# DB Close
connection.close()
print('DB CLOSED')