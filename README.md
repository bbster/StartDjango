# Python 설치
www.python.org 접속 -> 다운로드 메뉴 -> 버전 선택해서 다운로드 -> 다운로드 받은 파일 실행

-> 설치후 shell에서 python or python3 입력후 엔터 -> version 출력 확인

# MAC OS Pyenv install
brew install pyenv - pyenv 설치

brew upgrade pyenv - pyenv 업그레이드

https://github.com/yyuu/pyenv#basic-github-checkout

Pyenv path 설정

각자 환경에 맞게 .bash_profile 대신 .bashrc 혹은 .zshrc 로 적용한다.

$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile

$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile

$ echo 'eval "$(pyenv init -)"' >> ~/.bash_profile

$ source ~/.bash_profile

pyenv install --list   - 설치할수있는 버전 확인

pyenv install 버전명 ex) pyenv install 3.7.0

pyenv versions   - pyenv 버전 확인  // 출력 * system (set by PYENV_VERSION environment variable) 3.7.0

pyenv virtualenv 버전 가상환경이름 ex) pyenv virtualenv 3.7.0 practice_env


# MAC OS virtualenv install
각각의 다른 라이브러리가 설치된 가상환경을 가질수있고
사용자가 필요에 따른 다른 가상환경 접속가능 단점 사용자가 하나하나 기억


 pip3 -v  # pip 설치 확인

 sudo pip3 install virtualenv virtualenvwrapper #virtualenv 설치

 virtualenv --python=파이썬버전 가상환경이름  #ex) virtualenv --python=3.7.2 practice-env

 위에서 does not exsit가 뜨면 경로지정 오류

 whitch python3 -> 경로 -> virtualenv --python=경로 가상환경이름

 source 가상환경이름/bin/activate   #가상환경 진입
 

# MAC OS virtualenv Wrapper 사용
 위의 단점 보완
 VirtualenvWrapper를 사용할 경우 터미널이 현재 위치한 경로와 관계없이 가상환경을 활성화할 수 있다는 장점이 있습니다.

 cd ~ # 홈디렉터리로 이동

 mkdir ~/.virtualenvs  #폴더 생성

 export WORKON_HOME=~/.virtualenvs

 export VIRTUALENVWRAPPER_PYTHON="$(which python3)"  # Usage of python3

 source /usr/local/bin/virtualenvwrapper.sh

 mkvirtualenv 가상환경이름 # 가상환경 생성

 workon 가상환경이름 # 가상환경 접속

 (가상환경이름)$deactivate #가상환경 빠져나오기

# MAC OS Pyenv
brew install pyenv-virtualenv  # pyenv 설치

## ~/.bash_profile 파일에 아래 내용 추가
eval "$(pyenv init -)"

eval "$(pyenv virtualenv-init -)"

# WINDOWS virtualenv install
 pip install virtualenv

 virtualenv 가상환경이름 #가상환경 생성

 call 가상환경 경로   #ex)call c:\practice-env\Scripts\activate.bat # 가상환경 접속
 
 # Linux 추가예정

# Django 설치
 pip install django
 
 pip3 install django

# Django 프로젝트 생성
django-admin startproject 프로젝트명

# Django App 생성
djang-admin startapp 애플리케이션명

# Django 정상 실행 확인
python manage.py runserver (포트번호) //포트번호 안붙였을때 8000기본

# CRUD 예제
모델생성 -> makemigrations, migrate 명령어로 테이블생성 -> admin site 수정 -> 관리자 계정 생성 -> views 생성 -> url매칭

#CRUD 작성후 Django Rest Framework로 테스트

