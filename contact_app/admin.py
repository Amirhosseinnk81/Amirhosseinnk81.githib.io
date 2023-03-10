from django.contrib import admin
from .models import message
from .models import info
# Register your models here.

admin.site.register(message)
admin.site.register(info)
