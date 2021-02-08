from django.contrib import admin
from .models import User
from .models import EducationInstitution , EmailAddress

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

@admin.register(EducationInstitution)
class EducationInstitutionAdmin(admin.ModelAdmin):
    autocomplete_fields = ['parent']
    list_filter = ['isVerified', 'type']
    search_fields = ['name', 'slug']

@admin.register(EmailAddress)
class EmailAddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_email']
    list_filter = ['is_primary']