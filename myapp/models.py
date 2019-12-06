from django.db import models


# 모델 예제
class Book(models.Model):  # 클래스명은 대문자로
    name = models.CharField(max_length=50)
    picture = models.ImageField(blank=True)
    author = models.CharField(max_length=50, default='Anonymous')  # 저자
    email = models.EmailField(blank=True)
    describe = models.TextField(default='Practice', blank=True)  # 설명

    def __str__(self):
        return self.name
