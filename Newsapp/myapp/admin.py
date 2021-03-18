from django.contrib import admin
from .models import article
# Register your models here.
from django.contrib.auth.models import Permission

admin.site.register(article)
admin.site.register(Permission)