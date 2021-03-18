from django.contrib import admin
from .models import Comments
# Register your models here.
from django.contrib.auth.models import Permission

admin.site.register(Comments)
