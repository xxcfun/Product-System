from django.contrib import admin

# Register your models here.
from product import models

admin.site.register(models.Product)