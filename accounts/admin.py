from django.contrib import admin
from .models import User

# Register User model with the admin site
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Define fields to display in the list view of admin interface
    list_display = (
        'email',
        'username',
        'full_name',
        'phone',
        'is_superuser',
        'is_active',
    )

    # Define fields that are clickable to view details in the list view
    list_display_links = ('email', 'username', 'full_name')

    # Define fields for searching users in the admin interface
    search_fields = ('email', 'username', 'full_name')

    # Define fields that are readonly in the admin interface
    readonly_fields = ("date", "last_login")

    # Define ordering of users in the admin interface
    ordering = ('-date',)
