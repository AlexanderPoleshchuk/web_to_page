from django.db import models
from django.contrib.auth.models import User


class UrlResource(models.Model):
    url = models.URLField(max_length=256, blank=True, unique=True, verbose_name='Url resource')

    class Meta:
        verbose_name = 'Url resource'
        verbose_name_plural = 'Urls resource'

    def __str__(self) -> str:
        return self.url


class ApplicationProcessing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    create_datetime = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='Datetime')
    user_url = models.ForeignKey(UrlResource, blank=True, null=True, on_delete=models.CASCADE,
                                 verbose_name='Url resource for generate')
    task_id = models.CharField(max_length=250, blank=True, null=True, verbose_name='Task id')
    # STATUS_CHOICES = (
    #     (1, 'Data loading'),
    #     (2, 'In progress'),
    #     (3, 'Finish')
    # )
    status = models.CharField(max_length=100, blank=True, null=True, verbose_name='Status')
    finished_file = models.FileField(upload_to='documents/pdf', blank=True, null=True, db_index=True,
                                     verbose_name='Finished file pdf')

    class Meta:
        verbose_name = 'Application processing to pdf'
        verbose_name_plural = 'Application processing to pdf'

    def __str__(self) -> str:
        return f'Email-{self.user.email}; Status-{self.status}'
