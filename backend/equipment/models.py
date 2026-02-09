from django.db import models
from django.conf import settings

class EquipmentDataset(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    original_filename = models.CharField(max_length=255)
    total_records = models.IntegerField()
    avg_flowrate = models.FloatField()
    avg_pressure = models.FloatField()
    avg_temperature = models.FloatField()
    type_distribution = models.JSONField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"{self.original_filename} - {self.uploaded_at}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Keep only last 5 datasets per user
        datasets = EquipmentDataset.objects.filter(user=self.user).order_by('-uploaded_at')
        if datasets.count() > settings.MAX_DATASETS:
            # Get IDs of datasets to delete
            ids_to_delete = list(datasets.values_list('id', flat=True)[settings.MAX_DATASETS:])
            EquipmentDataset.objects.filter(id__in=ids_to_delete).delete()
