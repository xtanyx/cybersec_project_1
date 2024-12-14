from django.db import models

from django.contrib.auth.models import User

class Secret(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	secret = models.CharField(max_length=500)
