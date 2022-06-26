from django.db import models

from user.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField("카테고리 이름", max_length=20, unique=True)
    desc = models.CharField("카테고리 설명", max_length=255, null=True, blank=True)


class Article(models.Model):
    author = models.ForeignKey(
        "user.User", on_delete=models.SET_NULL, null=True)
    title = models.CharField("글 제목", max_length=100)
    category = models.ManyToManyField(to="Category", verbose_name="카테고리")
    content = models.TextField("글 내용")


class Comment(models.Model):
    article = models.ForeignKey(
        "Article", on_delete=models.CASCADE)
    user = models.ForeignKey(
        "user.User", on_delete=models.SET_NULL, null=True)
    content = models.TextField("댓글 내용")
