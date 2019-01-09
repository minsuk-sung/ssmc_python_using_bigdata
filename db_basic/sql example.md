# MySQL 간단한 사용방법

---

## 시작하기 앞서

### Sequel Pro
macOS에서 진행을 할 때, DB를 관리하는 툴로 `Sequel Pro`를 사용했다. 그리고 MySQL 말고 필자는 `MariaDB`로 넘어갔다. 
( 여담이지만, MySQL 문제인지 macOS의 문제인지 아니면 해당 어플리케이션의 문제인지는 모르겠으나, 자꾸 충돌이 일어나 제대로 작동을 안해서 애를 좀 먹었다. )

### SQL 파일 실행하기
아래 명령어를 통해서 테이블 생성과 데이터 입력까지 마친다.
```
mysql -u root -p
use python_db
mariaDB [(none)] > source /root/Desktop/test.sql 
```

---

## 조회
### users 테이블
회원이면 회원 데이터도 같이 보내는(추가)  
`*` 는 모든 컬럼을 다 가져오는 행위이므로

데이터가 많고 컬럼이 많으면 성능저하 원인
실제는 필요한것만 가져온다
```
select * from users;
```
특정 아이디와 특정 비번에 해당 되는 row 데이터

여기에 조건을 부여한다면
```
select *from users where uid='m' and upw='12';
select *from users where uid='m' and upw='1';
```

### tbl_trade 테이블

모든 데이터 조회하고 싶을 경우, 다음과 같은 쿼리문을 수행한다.
```
select *from tbl_trade;
```

10개만 제한해서 1페이지로 보여주고 싶을때, 다음과 같이 쿼리문을 작성한다.
```
select *from tbl_trade limit 10;

[1page]
select *from tbl_trade limit 0, 10;

[2page]
select *from tbl_trade limit 10, 10;

[3page]
select *from tbl_trade limit 20, 10;
```

최신순으로 보고 페이징, 이름순 정렬
```
select * from tbl_trade order by name asc;

select * from tbl_trade order by name desc;

select * from tbl_trade order by name desc limit 0,10;
```

게시물의 총 개수

> 총 페이지수는 = 총개수 / 페이지단위 수

ex) 10)+if 나머지가 존재하면 (1)
```
select count(*) from tbl_trade;

select count(name) as cnt from tbl_trade;
```

---

## 검색
"삼" 들어간 종목의 이름, 종목코드, 현재값만  가져오시오
```
select name, code, cur from tbl_trade where name like'%삼%'
```

'삼'으로 시작하는 종목이름만 가져오시오
```
select name, code, cur from tbl_trade where name like'삼%'
```

## 조인(inner Left,..), 유니온 등등