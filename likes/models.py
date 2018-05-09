from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from comments.models import Ownable
# Create your models here.
LIKE_TYPE = (
    (-1, '踩'),
    (0, '无'),
    (1, '顶'),
)

class Like(Ownable, models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    like_object = GenericForeignKey('content_type', 'object_id')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    status = models.SmallIntegerField(default=True)

    class Meta:
        verbose_name = '点赞'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.status:
            return '%s 赞了 %s的评论' % (self.owner.username, self.like_object)
        return '%s 踩了 %s的评论' % (self.owner.username, self.like_object)
