from django.contrib.auth.models import User
from django.db import models

from ckeditor.fields import RichTextField


class Event(models.Model):
    """Events displayed at main page and for attendance management."""

    title = models.CharField(max_length=100, verbose_name='标题')
    photo = models.ImageField(upload_to='event', blank=True, verbose_name='照片')
    body = RichTextField(blank=True, verbose_name='正文')
    link = models.URLField(blank=True, verbose_name='链接')
    created = models.DateField(auto_now_add=True, verbose_name='创建时间')
    is_headline = models.BooleanField(default=False, verbose_name='是否需要首页轮播')
    is_active = models.BooleanField(default=False, verbose_name='是否需要签到')
    attendees = models.ManyToManyField(
        User, blank=True, verbose_name='参与者', editable=False
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = '活动'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class News(models.Model):
    """News displayed at main page."""

    title = models.CharField(max_length=100, verbose_name='标题')
    photo = models.ImageField(upload_to='news', blank=True, verbose_name='照片')
    body = RichTextField(blank=True, verbose_name='正文')
    link = models.URLField(blank=True, verbose_name='链接')
    created = models.DateField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        ordering = ('-created',)
        verbose_name = '新闻'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
