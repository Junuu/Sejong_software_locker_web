# Sejong_software_locker_web
## 프로그램 설치 및 실행방법

- https://www.python.org/downloads/release/python-383/ 에서 운영체제에 맞는 python설치  
- https://dev.mysql.com/downloads/installer/ 에서 MySQL 설치
- sejong_locker_db.sql 을 MySQL에 import
- app.py 에서 db = pymysql.connect(host='localhost', port=3306, user= 'root', passwd='your_password, db='your_database') 비밀번호와 데이터베이스 이름 변경
- pip install flask
- pip install pymysql
- pip install bcrypt
- (if pip install bcrypt ERROR) 
- python -m pip install --upgrade pip 
- python -m pip install --no-use-pep517 bcrypt
- (else)
-  python app.py 실행

## 프로그램 설명
- Python Flask server와 Mysql을 사용하여 만든 소프트웨어학과 사물함 웹사이트입니다.
- 페이지는 홈, 회원가입, 로그인 으로 구성되어 있으며 UI측면에서 모바일, 테블릿에서도 사용하기 편하도록 제작되었습니다.
- 회원가입, 로그인 이후에 홈 화면에서 사용 가능한 사물함을 클릭하면 사물함을 신청할 수 있습니다.
- 홈 화면에서 현재 자신이 어느 사물함을 사용하고 있는지 알 수 있습니다.
- 만약 현재 자신이 사용중인 사물함을 클릭하면 사물함을 반납할 수 있습니다.
- 사물함은 1개만 이용 가능하며 그 이외에 고장난 사물함, 다른 사람이 사용중인 사물함에는 접근할 수 없습니다.
