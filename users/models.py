from django.db import models
from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    """
    用户资料,仅仅存储Profile信息,但是包含头像
    telephone
    password
    register_source
    register_time
    is_active
    is_social
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='profile',
        on_delete=models.CASCADE,
        primary_key=True)

    username = models.CharField(
        '用户名',
        max_length=150,
        unique=True,
        help_text='',
        validators=[
            # username_validator
            # TODO : 这里需要用户名和密码
        ],
        error_messages={
            'unique': "用户名已重复",
        },
    )
    telephone = models.CharField(max_length=20, blank=True, db_index=True, null=True, unique=True, verbose_name="手机")
    avatar_url = models.URLField(max_length=255, blank=True, verbose_name="头像链接")

    register_source = models.CharField(max_length=10, default=0, verbose_name="注册来源")
    register_time = models.DateTimeField(auto_now_add=True, verbose_name="注册时间")

    REQUIRED_FIELDS = ['telephone']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return '<Account # %d, %s>' % (self.id, self.username)

    @property
    def avatar(self):
        if not self.avatar_url:
            return settings.AVATAR_URL_PREFIX + settings.DEFAULT_AVATAR

    class Meta:
        verbose_name = "用户账号"
        verbose_name_plural = "用户账号"
