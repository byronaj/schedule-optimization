from django.contrib import admin

from .models import Employee


admin.site.register(Employee)

# TODO: add schedule and other models to make them show up in django admin
# admin.site.register(Schedule)
