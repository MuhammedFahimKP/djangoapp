from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CUser,Product


class CUseradmin(UserAdmin):
    
    list_display=('email','date_joined','last_login','is_staff','is_superuser')
    list_display_links=('email',)

    filter_horizontal=()
    list_filter=()
    fieldsets=()
    
admin.site.register(CUser, CUseradmin)

admin.site.register(Product)
# Register your models here.
