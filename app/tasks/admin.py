from django.contrib import admin

from .models import CalcResult, Params

# Register your models here.

admin.site.register(Params)
admin.site.register(CalcResult)
