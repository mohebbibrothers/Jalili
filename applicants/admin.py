from django.contrib import admin
from .models import Applicant

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'national_code', 'phone_number', 'type')
    search_fields = ('name', 'last_name', 'national_code', 'phone_number', 'type')