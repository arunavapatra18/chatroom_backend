from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _

from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    # Fields to display in the admin panel when creating a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    
    # Fields to display in admin panel in different sections when modifying an existing user
    fieldsets = (
        (None, {"fields": ('username', 'email', 'password')}),
        (_('Permissions'),  {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important data'), {'fields': ('last_login', 'date_joined')}),
    )
    