from django.db import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    email = models.EmailField(unique=True)
    web_site = models.CharField(max_length=255, blank=True)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []