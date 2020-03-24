from django.db import models
from user.models import UserProfile


# Create your models here.


class Blog(models.Model):

    author = models.ForeignKey(UserProfile)
    article = models.TextField(verbose_name='文章')
    article_class = models.CharField(max_length=15, verbose_name='文章类型')
    title = models.CharField(max_length=20, verbose_name='文章标题')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    reading_volume = models.IntegerField(verbose_name='阅读量')
    comment_volume = models.IntegerField(verbose_name='评论量')
    like_volume = models.IntegerField(verbose_name='点赞量')

    class Meta:
        db_table = 'blog_blog'


class Comment(models.Model):

    author = models.ForeignKey(UserProfile)
    comment = models.TextField(verbose_name='评论')
    id_comment_with = models.IntegerField(verbose_name='被评论的id')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    like_volume = models.IntegerField(verbose_name='点赞量')
    blog = models.ForeignKey(Blog)

    class Meta:
        db_table = 'blog_comment'
