from django.db import models
from django.utils.timezone import now


class CommonSwaggerCoverage(models.Model):
    project = models.CharField(max_length=64)
    full_coverage = models.FloatField()
    partial_coverage = models.FloatField()
    empty_coverage = models.FloatField()
    actual_cnt = models.PositiveIntegerField(default=0)
    full_cnt = models.PositiveIntegerField(default=0)
    partial_cnt = models.PositiveIntegerField(default=0)
    empty_cnt = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f'{self.project} project has full api coverage {self.full_coverage} {self.full_cnt}/{self.actual_cnt})%'
