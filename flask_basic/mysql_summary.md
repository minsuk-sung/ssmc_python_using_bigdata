# 삼성멀티캠퍼스 빅데이터를 활용한 파이썬 프로그래밍

## Part3. 데이터베이스( DataBase )

RDMBS <-> NoSQL

1. RDMBS : 관계형 데이터 베이스 관리 시스템  
SQL 공부해서 **쿼리(query)수행**하여 조작(**데이터 추가,삭제,수정,조회** : CRUD)
    - 엔터급 : 오라클,MSSQL,오로라,...
    - 개발급 : MySQL,마리아,...

 2. NoSQL : JSON, log, BigData ... 추후에 정말 큰 데이터들은 이쪽으로 가야할 것
    - 몽고DB

#### 개발환경 구축

필자는 어떠한 이유인지는 몰라도 `MySQL`을 데이터 베이스 관리툴인 `Sequel Pro`와 연동하는 과정에서 충돌이 발생해서 `MariaDB`로 대체하였다. MySQL과 MariaDB는 크게 무리없이 문법이 호환된다고 한다. MariaDB의 설치는 다음과 같다.
```
brew install mariadb
```

설치가 완료되면 다음과 같은 명령을 수행한다.
```
mysql.server start
```

그리고 다음과 같은 명령어를 통해서 비밀번호를 설정한다. 이때 순서대로 no -> 비번입력 -> y -> y -> n -> y 로 입력하자.
```
mysql_secure_installation
```

로그인을 하기 위해서 다음과 같은 명령어를 수행하자
```
mysql -u root -p
```

#### 파이썬을 통한 데이터베이스 연동

파이썬을 통해서 MySQL 연동하고자 할때 쓰는 패키지는 `PyMySQL`이다. 이걸 통해서 간단하게 연동시킬 수 있다. 다음과 같은 명령어를 통해서 설치하자
```
pip install pymysql
```

간단한 포맷은 다음과 같다.
```python
import pymysql as pms

def simplefunc():
    connection = None
    rows       = None 

    try:
        # DB와 연동하는 부분
        connection = pms.connect(   host='localhost', # 디비 주소
                                    user='root', # 디비 접속 계정
                                    password='1234', # DB 접속 비번
                                    db='user_db', # DB 이름
                                    # port=3306, # 설정한 포트 (기본은 3306)            
                                    charset='utf8', # DB의 데이터 포맷들
                                    cursorclass=pms.cursors.DictCursor) # 커서타입지정
        # 쿼리 수행하는 부분
        with connection.cursor() as cursor:            
            sql = ''' 원하는 쿼리 수행 ''' # 쿼리는 여러줄이므로 '''로 하는걸 권장
            cursor.execute( sql )
            # 여러개 데이터를 다 가져올때
            rows    = cursor.fetchall()

    except Exception as e:
        print('->', e)
        rows = None

    finally:
        if connection:
            connection.close()

    return rows
```
이걸 응용해서 DB와 연동하도록 하자.