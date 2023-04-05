from django.db import models

class UserModel(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name or ''
