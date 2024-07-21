from django.db import models

# Create your models here.
class Member(models.Model):
    loginId = models.CharField(max_length=16)
    access_token = models.CharField(max_length=512)
    expired_date = models.DateTimeField()
    access_token_type = models.CharField(max_length=20)
    expires_in = models.IntegerField()
    
    def __str__(self):
        return self.loginId