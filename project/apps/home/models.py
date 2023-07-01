from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    # Otros campos de perfil

    def _str_(self):
        return self.user.username
