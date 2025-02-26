from django.contrib import admin

from .models import Department, Staff, Status

admin.site.register(Department)
admin.site.register(Staff)
admin.site.register(Status)