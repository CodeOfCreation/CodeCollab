from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    # Add custom fields to the admin interface
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('bio', 'reputation_score', 'avatar')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('bio', 'reputation_score', 'avatar')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)