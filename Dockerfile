# 배포 환경
# docker bild -t name . // 빌드 명령어
# docker run --name 컨테이너명 -itd
# --restart unless-stopped 서비스가 꺼지지않게
# 이미지명
FROM python:3.8.0

RUN pip install django
RUN pip install djangorestframework

