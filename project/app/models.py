from django.db import models
# Create your models here.


class Users(models.Model):
    uname = models.CharField(max_length=20)
    score = models.CharField(max_length=20)

    class Meta():
        db_table = 'users'

class Rank(models.Model):
    rankNum = models.IntegerField()
    user = models.OneToOneField(Users, on_delete=models.CASCADE)

    class Meta():
        db_table = 'rank'
