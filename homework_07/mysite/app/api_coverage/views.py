from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CommonSwaggerCoverage
from .serializers import APICoverageSerializerserializers


class ApiCoverageView(APIView):
    def get(self, request):
            api_coverage = CommonSwaggerCoverage.objects.all()
            serializer = APICoverageSerializerserializers(api_coverage, many=True)
            return Response({"api_coverage": serializer.data})
    
    def post(self, request):
        api_coverage = request.data
        serializer = APICoverageSerializerserializers(data=api_coverage)
        if serializer.is_valid(raise_exception=True):
            api_coverage_saved = serializer.save()
        return Response({"success": f"Coverage for project '{api_coverage_saved.project}' created successfully"})