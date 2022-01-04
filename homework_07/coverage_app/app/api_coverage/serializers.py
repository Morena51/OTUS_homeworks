from rest_framework import serializers
from django.utils.timezone import now

from .models import CommonSwaggerCoverage


class APICoverageSerializerserializers(serializers.Serializer):
    project = serializers.CharField(max_length=64)
    full_coverage = serializers.FloatField()
    partial_coverage = serializers.FloatField()
    empty_coverage = serializers.FloatField()
    actual_cnt = serializers.IntegerField(default=0)
    full_cnt = serializers.IntegerField(default=0)
    partial_cnt = serializers.IntegerField(default=0)
    empty_cnt = serializers.IntegerField(default=0)
    created_at = serializers.DateTimeField(default=now)

    def create(self, validated_data):
        return CommonSwaggerCoverage.objects.create(**validated_data)

