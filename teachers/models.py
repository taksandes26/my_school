from django.db import models


# Create your models here.
class Teachers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True)
    phone = models.SmallIntegerField(max_length=10, unique=True)
    designation = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"

    class Meta:
        verbose_name_plural = "Teachers"
