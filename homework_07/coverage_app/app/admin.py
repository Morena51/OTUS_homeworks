from django.contrib import admin
from .models import Project, APICoverage, E2ECoverage, UnitCoverage
# Register your models here.

admin.site.register(Project)
admin.site.register(APICoverage)
admin.site.register(E2ECoverage)
admin.site.register(UnitCoverage)
