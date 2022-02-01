from django.contrib import admin
from .models import Couriers


class SettingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Couriers._meta.get_fields()]


admin.site.register(Couriers, SettingAdmin)

# Register your models here.
