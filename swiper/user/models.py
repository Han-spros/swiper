from django.db import models

# Create your models here.

class User(models.Model):
    SEXS = ((0, '未知'), (1, '男'), (2, '女'))
    LOCATIONS = (('gz', '广州'), ('sz', '深圳'), ('sh', '上海'), ('bj', '北京'), ('cq', '重庆'))
    phonenum = models.CharField(max_length=11, unique=True)
    nickname = models.CharField(max_length=16)
    sex = models.IntegerField(choices=SEXS, default=0)
    birth_year = models.IntegerField(default=2000)
    birth_month = models.IntegerField(default=1)
    birth_day = models.IntegerField(default=1)
    avatar = models.CharField(max_length=256)
    location = models.IntegerField(choices=LOCATIONS, default='cq',max_length=12)

    class Meta:
        db_table = 'users'