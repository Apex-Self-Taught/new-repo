from django.db import models

# Create your models here.


class StoreHooksData(models.Model):
    username = models.CharField(max_length=200)
    user_id = models.IntegerField(unique=True)
    avatar_url = models.CharField(max_length=1000)