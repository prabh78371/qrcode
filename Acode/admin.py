from django.contrib import admin
from .models import modelqrp

# Register your models here.
@admin.register(modelqrp)
class qradmin(admin.ModelAdmin):
    list_display = ['id','name','code']
