"""
 参考:https://github.com/r26zhao/django-easy-comment/
"""
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

from mptt.models import TreeForeignKey, MPTTModel

# Create your models here.

class Ownable(models.Model):
    """
    Abstract model that provides ownership of an object for a user.
    """

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                              null=True, verbose_name="用户", related_name="%(class)ss")

    class Meta:
        #允许继承
        abstract = True

    def is_editable(self, request):
        """
        Restrict in-line editing to the objects's owner and superusers.
        """
        return request.user.is_superuser or request.user.id == self.owner_id


class Orderable(models.Model):
    order_num = models.IntegerField("排序", null=True)

    class Meta:
        # 允许继承
        abstract = True


class Comment(Ownable, MPTTModel):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    comment_object = GenericForeignKey('content_type', 'object_id')
    parent = TreeForeignKey('self', blank=True, null=True, verbose_name='父级评论')
    content = models.TextField(max_length=2250, blank=True, null=True, verbose_name='评论内容')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    update_date = models.DateTimeField(auto_now=True, verbose_name="更新日期")

    class MPTTMeta:
        verbose_name = ' 评论'
        verbose_name_plural = verbose_name
        order_insertion_by = ('create_date')

    def __str__(self):
        if self.parent is not None:
            return '{} 回复 {}'.format(self.owner.username, self.parent.owner.username)
        return '{} 评论 实体 {}'.format(self.owner.username, self.parent.owner.username)
