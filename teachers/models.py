from django.db import models


# Create your models here.
class teachers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.BigIntegerField()
    designation = models.CharField(max_length=50)

    def __str__(self):
        return self.last_name
