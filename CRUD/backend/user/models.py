from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100, null=True, blank=True)
    age = models.PositiveIntegerField()
    qualification = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        db_table = 'users'

    def __str__(self):
        return f"{self.name} ({self.mobile_number})"