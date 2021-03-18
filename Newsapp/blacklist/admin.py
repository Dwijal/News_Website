from django.contrib import admin
from .models import Blacklist
# Register your models here.
from django.contrib.auth.models import Permission

admin.site.register(Blacklist)
