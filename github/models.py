from django.contrib.auth.models import User
from django.db import models


class UserGithub(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    gh_username = models.TextField(null=False, blank=False)
    oauth_token = models.TextField(null=True, blank=True)
