from django.db import models

from blogs.es_doc import BlogIndexDoc
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=125, unique=True, verbose_name='名称')
    order_num = models.IntegerField(verbose_name="排序", default=0, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    update_date = models.DateTimeField(auto_now=True, verbose_name="更新日期")

    class Meta:
        verbose_name = '类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=125, unique=True, verbose_name='名称')
    order_num = models.IntegerField(verbose_name="排序", default=0, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    update_date = models.DateTimeField(auto_now=True, verbose_name="更新日期")

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Blog(models.Model):
    category = models.ForeignKey(Category, related_name="category_blogs", null=True, on_delete=models.SET_NULL,
                                 verbose_name="类型")
    title = models.CharField(max_length=125, blank=True, null=True, verbose_name='标题')
    content = models.TextField(max_length=2550, blank=True, verbose_name='内容')
    char_num = models.IntegerField(verbose_name="字数统计", default=0)
    is_published = models.BooleanField(default=True, verbose_name='是否发布')
    is_comments_enabled = models.BooleanField(verbose_name="允许评论", default=True)
    like_numbers = models.IntegerField(verbose_name="点赞数量", default=0)
    tag = models.ManyToManyField(Tag, verbose_name="标签", related_name="tag_blogs")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    update_date = models.DateTimeField(auto_now=True, verbose_name="更新日期")

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = verbose_name

    def display_tag_name(self):
        """
        Creates a string for the Tag. This is required to display tag in Admin.
        Admin:列出tag字段
        """
        return ', '.join([genre.name for genre in self.tag.all()])
    display_tag_name.short_description = '标签'


    def create_es_blog_index_doc(self, **kwargs):
        """
        创建Blog索引、文档, 并存入elasticsearch数据库
        :return:
        """
        obj = BlogIndexDoc(
            meta={'id': self.id},
            title=self.title,
            content=self.content,
            char_num=self.char_num,
            is_comments_enabled=self.is_comments_enabled,
            like_numbers=self.like_numbers,
            category=self.category.name,
            tags=",".join([tag.name for tag in self.tag.all()]),
            suggestions={"input": [tag.name for tag in self.tag.all()]},
            create_date=self.create_date
        )
        obj.save()
        print("创建索引成功, {}".format(obj.to_dict(include_meta=True)))
        return obj.to_dict(include_meta=True)

    def __str__(self):
        return "{} - {}".format(self.title, self.create_date)