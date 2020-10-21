from django.contrib import admin

# Register your models here.
from record import models

admin.site.register(models.Record)
