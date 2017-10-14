from django.conf import settings
from django.db import models


class Profile(models.Model):
    """Stores detailed information of a user."""

    # Sex choices
    MALE = 'M'
    FEMALE = 'F'
    UNKNOWN = 'U'

    SEX_CHOICES = {
        (MALE, '男'),
        (FEMALE, '女'),
        (UNKNOWN, '未选择'),
    }

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    full_name = models.CharField(max_length=10, blank=True, verbose_name='姓名')
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
        default=UNKNOWN,
        verbose_name='性别',
    )
    identity = models.CharField(max_length=50, blank=True, verbose_name='身份')
    college = models.CharField(max_length=50, blank=True, verbose_name='学院')
    major = models.CharField(max_length=50, blank=True, verbose_name='专业')
    avatar = models.ImageField(
        upload_to='users/avatars', blank=True, verbose_name='头像'
    )

    class Meta:
        verbose_name = '个人档案'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}的详细信息'.format(self.user.username)
