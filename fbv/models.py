from django.db import models


# 모델 예제
class Song(models.Model):  # 클래스명은 대문자로
    name = models.CharField(max_length=50)
    lyrics = models.TextField(default='input lyrics', blank=True)  # 설명

    def __str__(self):
        return self.name
