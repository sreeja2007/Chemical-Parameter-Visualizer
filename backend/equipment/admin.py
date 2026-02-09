from django.contrib import admin
from .models import EquipmentDataset

@admin.register(EquipmentDataset)
class EquipmentDatasetAdmin(admin.ModelAdmin):
    list_display = ['original_filename', 'uploaded_at', 'total_records', 'user']
    list_filter = ['uploaded_at']
    search_fields = ['original_filename']
