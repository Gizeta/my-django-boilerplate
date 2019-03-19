from django.db import models

class User(models.Model):
  class Meta:
    db_table = 'user'

  username = models.CharField('用户名', max_length=20, unique=True)
  password = models.CharField('密码', max_length=32)
  