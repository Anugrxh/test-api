from django.db import models

# Create your models here.
from django.db import models

class UserInfo(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname
