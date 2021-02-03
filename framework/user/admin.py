from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    ##show how each object will be listed
    list_display = ['username', 'date_joined']
    ##show filters
    list_filter = [
        'is_active', 'is_staff', 'gender', 'date_joined'
    ]
    ##seach fields
    search_fields = ['username', 'first_name', 'last_name', 'email']

