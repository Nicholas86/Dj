from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=125, unique=True, verbose_name='博客类型')
    order_num = models.IntegerField(verbose_name="排序", default=0, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    update_date = models.DateTimeField(auto_now=True, verbose_name="更新日期")

    class Meta:
        verbose_name = '类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=125, unique=True, verbose_name='标签名称')
    order_num = models.IntegerField(verbose_name="排序", default=0, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    update_date = models.DateTimeField(auto_now=True, verbose_name="更新日期")

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=125, blank=True, null=True, verbose_name='标题')
    description = models.TextField(max_length=2550, blank=True, verbose_name='内容')
    is_published = models.BooleanField(default=True, verbose_name='是否发布')
    is_comments_enabled = models.BooleanField(verbose_name="允许评论", default=True)
    like_numbers = models.IntegerField(verbose_name="点赞数量", default=0)
    category = models.ForeignKey(Category,related_name="category_blogs", null=True, on_delete=models.SET_NULL,
                                 verbose_name="类型",)
    tags = models.ManyToManyField(Tag, verbose_name="标签", related_name="tag_blogs")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    update_date = models.DateTimeField(auto_now=True, verbose_name="更新日期")

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{} - {}".format(self.title, self.create_date)