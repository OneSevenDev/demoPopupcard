from django.contrib.auth.models import User
from django.db import models

from business.base.models import BaseEntity

# Create your models here.
def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Persona(BaseEntity, models.Model):
    avatar = models.ImageField(upload_to=user_directory_path)
    user = models.OneToOneField(User)
    gender = models.CharField(max_length=200)
    birth_date = models.DateField('+birth_date', null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)