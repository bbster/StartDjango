# MAC OS virtualenv install
각각의 다른 라이브러리가 설치된 가상환경을 가질수있고
사용자가 필요에 따른 다른 가상환경 접속가능 단점 사용자가 하나하나 기억

'''
 pip3 -v  # pip 설치 확인

 sudo pip3 install virtualenv virtualenvwrapper #virtualenv 설치

 virtualenv --python=파이썬버전 가상환경이름  #ex) virtualenv --python=3.7.2 practice-env

 위에서 does not exsit가 뜨면 경로지정 오류

 whitch python3 -> 경로 -> virtualenv --python=경로 가상환경이름

 source 가상환경이름/bin/activate   #가상환경 진입
 '''

# MAC OS virtualenv Wrapper 사용
 위의 단점 보완
 VirtualenvWrapper를 사용할 경우 터미널이 현재 위치한 경로와 관계없이 가상환경을 활성화할 수 있다는 장점이 있습니다.
'''
 cd ~ # 홈디렉터리로 이동

 mkdir ~/.virtualenvs  #폴더 생성

 export WORKON_HOME=~/.virtualenvs

 export VIRTUALENVWRAPPER_PYTHON="$(which python3)"  # Usage of python3

 source /usr/local/bin/virtualenvwrapper.sh

 mkvirtualenv 가상환경이름 # 가상환경 생성

 workon 가상환경이름 # 가상환경 접속

 (가상환경이름)$deactivate #가상환경 빠져나오기
'''

# WINDOWS virtualenv install
 pip install virtualenv

 virtualenv 가상환경이름 #가상환경 생성

 call 가상환경 경로   #ex) c:\practice-env\Scripts\activate.bat # 가상환경 접속

# Django 설치
 pip install django
 pip3 install django
 
# Django 3.0 업데이트로 인해 python 3.6이상 설치


# Django 프로젝트 생성
django-admin startproject 프로젝트명

# Django 정상 실행 확인
python manage.py runserver (포트번호) 포트번호 안붙였을때 8000기본

# CRUD 예제
모델생성 -> makemigrations, migrate 명령어로 테이블생성 -> admin site 수정 -> 관리자 생성 -> views 생성 
 -> template 생성 or postman 같은 프로그램으로 테스트

