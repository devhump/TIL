from django.db import models

# Create your models here.
class Review(models.Model):
    # 리뷰 제목
    title = models.CharField(max_length=80)
    # 리뷰 내용
    content = models.TextField(null=True)
    # 할 일 생성시간
    created_at = models.DateTimeField(auto_now_add=True)
    # 할 일 수정시간
    updated_at = models.DateTimeField(auto_now=True)