from rest_framework import serializers
from .models import EquipmentDataset

class EquipmentDatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentDataset
        fields = ['id', 'uploaded_at', 'original_filename', 'total_records', 
                  'avg_flowrate', 'avg_pressure', 'avg_temperature', 'type_distribution']
        read_only_fields = ['id', 'uploaded_at']
