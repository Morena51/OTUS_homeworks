from django.contrib import admin
from .models import Project, APITest, E2ETest, UnitTest
# Register your models here.

admin.site.register(Project)
admin.site.register(APITest)
admin.site.register(E2ETest)
admin.site.register(UnitTest)
