# 삼성멀티캠퍼스 빅데이터를 활용한 파이썬 프로그래밍

## Part2. 파이썬 웹프로그래밍 ( Web Programming ) 

#### 웹프로그램의 구성
파이썬으로 데이터 수집, 데이터 전처리, 데이터 분석, 레포트, 소프트웨어까지 전개할 수 있는데 분석 후 시각화 및 응용 서비스 제공 차원에서 웹을 활용할 수 있다. 프로젝트 결과물을 **웹으로 보여주는 수단**이라고 생각하면 된다.

#### 기업체에서 활용
동일한 언어로 구성된 시스템 마이그레이션의 대상으로 파이썬 웹을 활용한다.
> Spring -> Python, Nodejs -> Python

#### 데이터 크롤링
웹에서 데이터를 획득하여 전처리후 의미있는 데이터로 수집하는 방법을 이해를 해야한다. 이를 위해서는 **html,css,자바스크립트에 대한 이해가 필요**하다. 특히 자바스크립트에 대한 이해가 중요하다. 서비스 관점에서도 GUI 구성이 가능해야 한다. qt5 패키지를 공부해야한다. 이걸 위해서는 웹을 잘 이해해야한다.
> Python Django or Flask

#### 웹 환경 이해
클라이언트와 서버 간의 관계, 통신에 관련된 간략한 흐름을 알 수 있는 모델인 OSI 7 Layer

---

### 파이썬 패키지 목록 확인
Terminal을 통해서 현재 python 3.X 환경에 설치된 패키지 목록 확인을 위해 아래와 같은 명령어를 통해서 실행하자
```
Windows 10
pip list

macOS
$ pip3 list
```

### Flask 설치
만약 위를 통해 확인한 결과 flask가 없다면, 아래와 같은 명령어를 통해서 실행하자
```
pip install flask
```

### 가상 환경 구축
가상환경 `virtualenv` 환경에서 통상 설치 개발한다. 이는 **개발 환경(OS)과 운용환경(AWS, Docker)을 통일하게 맞추기 위한 절차**이다. 당장 영향 받는 부분이 없어서 일단 로컬에서 설치한다. 이 부분은 차후에 변경할 예정이다.

---

### Flask의 기본
일단 어떻게 시작해야할지 모르겠다면, 다음과 같은 코드를 작성하고 해당 파이썬 파일을 실행해보자. 이 함수의 결과는 **로컬호스트(http://127.0.0.1)을 통해서 확인**할 수 있다.
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello world!'

app.run(debug=True)
```

여기에 다른 홈페이지를 하나 추가해보자.그러기 위해서는 기본 틀에 해당 코드를 추가하자. 그러면 http://127.0.0.1/test 에서 확인할 수 있다.
```python
@app.route('/test')
def test():
    return 'test page'
```

### 동적파라미터


---

### 배포하기전 
#### AWS 계정 생성하기

#### 사전 조치 
1. EC2에 생성한 서버를 잡고 우클릭
2. 연결 > 연결정보창을 띠워놓고

* 맥유저
    1. Terminal 오픈
    2. pem파일이 위치한 경로로 이동
    ```
    cd C:\Users\student\Desktop\aws
    ```
    3. 퍼미션 조정
    ```
    chmod 400 내가생성한키.pem 
    ```
    4. 접속
    ```
    ssh -i "gemoney.pem" ubuntu@ec2-13-209-69-38.ap-northeast-2.compute.amazonaws.com
    ```
    5. yes

* 윈도우 유저
    1. putty.exe, puttyGen.exe 파일 다운로드
    2. puttyGen.exe > LOAD 클릭 > ***.pem 선택 (*.*선택) 
    > save private key > ***.ppk 이름으로 저장
    3. putty.exe 실행
    > host name 항목 기입
        ubuntu@ec2-13-125-181-222.ap-northeast-2.compute.amazonaws.com
    > 세션이름 설정후 (ex) aws) > save
    > conecction > ssh > auth > C:\Users\student\Desktop\aws\gemoney.ppk
        설정
    > session > save
    > open > 예 > 

### 우분트 리눅스에서 flask로 만든 서비스 배포 밑 운영

#### 1.터미널 혹은 PuTTY를 통해 접속 후 버전 확인
```
cat /etc/issue
```
Ubuntu 18.04.1 LTS \n \l

---

#### 2.파이썬 버전 확인
```
python3 --version
```
Python 3.6.5

---

#### 3. 해당 서버에서 필요한 작업들

##### root 권한 획득 
```
sudo su
```

##### 권한을 빠져 나간다 => root 로그아웃
```
exit
```

현재프럼프트는 아래와 같이 나올 것
```
ubuntu>
```

해당 계정에서 root 권한 명령으로 뭔가 하고 싶으면 (관리자 권한 실행하자)( nginx는 웹서버임 ( apache, ngninx 등등 ) )
```
ubuntu>sudo apt-get update 
ubuntu>sudo apt-get upgrade
ubuntu>sudo apt-get install python3-pip python3-dev nginx
```

##### 가상환경구축 : virtualenv 설치
```
sudo pip3 install virtualenv
```

##### 가상환경을 만들 디렉토리
디렉토리 생성
```
mkdir ~/flasksvr
```
  
디렉토리 이동
```
cd ~/flasksvr
```

가상환경 생성
```
virtualenv -p python3 flasksvrenv
```

가상환경 활성화
```
source flasksvrenv/bin/activate
```
활성화가 끝나면 아래와 같이 나온다
```
(flasksvrenv) ubuntu#~...$ 
```

#####  Fileziller를 이용하여 ftp 접속 및 파일 업로드 처리 가능
디렉토리 구조나 퍼미션 정보도 같이 볼수 있다
> 구글>검색>다운로드(프리버전)>설치 
> /home/ubuntu/flasksvr 밑에 flask_ex.tar 파일 업로드(드레그)

##### 현재 설치 목록
```
pip list
```
이 중에 uwsgi를 설치하여 aws서버에서 계속 돌아갈 수 있게 만들어주자
uwsgi => 운영관련 모듈
```
pip install flask uwsgi
```

현재 위치 확인
```
ls
```
파일 생성 -> 편집 -> vi, nano, vim등등
다음과 같이 run.py로 
```
nano run.py
```

아래와 같은 코드를 작성한다.
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hi Flask</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0')  
```
포트 5000번 오픈하고 실행
```
sudo ufw allow 5000
python run.py
```

터미널을 닫고 나가면 서버가 종료되서 서비스가 중단된다. 서버 개발자가 항상 서버를 바라볼수 없으므로, 백그라운드에서 서비스가 구동되게 구성을 해야한다  
=> **uwsgi 모듈을 이용하여 처리 + 서비스 구동 + nginx 연동**

---

#### 4. uWSGI 구성
entry point 생성(진입로-> 서버의 시작점)하기 위해 `wsgi.py`를 만들자. 
```
sudo nano ~/flasksvr/wsgi.py
```
그리고 아래와 같은 명령어를 작성하자
```python
from run import app
if __name__ == '__main__':
    app.run()
```
 
##### 구동 (단독구동시)
```
uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app
```

##### flask 서버종료
`ctrl + c`

##### 가상환경 나오기
`deactivate`

---

#### 5. 서비스 구성을 위한 작업
서비스 구성을 위한 ini파일을 만들어보자
```
nano ~/flasksvr/flasksvr.ini
```

그리고 다음과 같은 내용을 작성하자
```
[uwsgi]
module = wsgi:app

master = true
processes = 5

socket = flasksvr.sock
chmod-socket = 660
vacuum = true

die-on-term = true
```

##### systemd unit file  생성
server 부팅될때 자동으로 uwsgi가 가동되서 서버가 정상운영된다.
```
sudo nano /etc/systemd/system/flasksvr.service
```
다음과 같은 명령어를 친다.
```
[Unit]
Description=uWSGI instance server
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/flasksvr
Environment="PATH=/home/ubuntu/flasksvr/flasksvrenv/bin"
ExecStart=/home/ubuntu/flasksvr/flasksvrenv/bin/uwsgi --ini flasksvr.ini

[Install]
WantedBy=multi-user.target
```

##### 실행 및 활성화
생성한 flasksvr 서비스을 위해서 다음과 같은 명령어를 실행한다.
```
sudo systemctl start flasksvr
sudo systemctl enable flasksvr
```

##### nginx 연동처리
nginx 연동을 위하여 다음과 같은 명령어를 진행하자
```
sudo nano /etc/nginx/sites-available/flasksvr
```

그리고 아래와 같은 내용을 작성하자
```
server {
  listen 80;
  server_name 54.180.153.100;

  location / {
    include uwsgi_params;
    uwsgi_pass unix:///home/ubuntu/flasksvr/flasksvr.sock;
  }
}
```

##### 링크설정
```
sudo ln -s /etc/nginx/sites-available/flasksvr /etc/nginx/sites-enabled
```

##### 설정에대한문법체크
```
sudo nginx -t
```

##### nginx 재가동 
```
sudo systemctl restart nginx
```

##### 링크설정
```
sudo ln -s /etc/nginx/sites-available/flasksvr /etc/nginx/sites-enabled
```

##### 설정에대한문법체크
```
sudo nginx -t
```

##### nginx 재가동 
```
sudo systemctl restart nginx
```

##### 5000포트닫고, nginx sevrer 접속허용
```
sudo ufw delete allow 5000
sudo ufw allow 'Nginx Full'
```
 
##### 서비스로그 확인
```
systemctl -l status flasksvr
```
 
##### 코드수정후명령
```
sudo systemctl restart flasksvr
```
 
##### nginx log
```
tail -f /var/log/nginx/error.log
```