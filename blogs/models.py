from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=125, blank=True, null=True, verbose_name='标题')
    description = models.TextField(max_length=2550, blank=True, verbose_name='内容')
    is_published = models.BooleanField(default=True, verbose_name='是否发布')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    update_date = models.DateTimeField(auto_now=True, verbose_name="更新日期")

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = verbose_name