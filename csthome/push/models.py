from django.db import models


class PushNotification(models.Model):
    """Push notification model."""

    content = models.TextField(max_length=100, verbose_name='内容')
    has_pushed = models.BooleanField(default=False,
                                     editable=False,
                                     verbose_name='是否已推送')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '推送通知'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content
