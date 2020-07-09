from django.db import models

# Create your models here.
class Number(models.Model):
    author=models.CharField('Author',max_length=100)
    picture = models.CharField('Picture', max_length=250)
    need_to_find = models.CharField('Need to find', max_length=100)
    found = models.CharField('Found', max_length=100)
    time_upload = models.TimeField('Upload time',auto_now_add=True)
    work_time = models.TimeField('Work time')

    def __str__(self):
        return self.author
