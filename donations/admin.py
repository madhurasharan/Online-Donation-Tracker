from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Donation

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('campaign', 'donor', 'amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('campaign__title', 'donor__username')
