from django.db import models


class Feedback(models.Model):
    """Users feedback on this app."""

    body = models.TextField(verbose_name='内容')
    created = models.DateTimeField(auto_now_add=True, verbose_name='时间')

    class Meta:
        ordering = ('-created',)
        verbose_name = '意见反馈'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.body
