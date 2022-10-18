from django.db import models

class Users(models.Model):
    user_id = models.CharField(max_length=10, null=False)
    nickname = models.CharField(max_length=15, null=False)
    data_reg = models.DateTimeField(auto_now_add=True)
    info_user = models.CharField(max_length=100)

