from django.contrib import admin


# Register your models here.
from applications.ps1.models import Stock,IndentFile
admin.site.register(Stock)
admin.site.register(IndentFile)