from django.db import models
from django.utils.timezone import now


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True


class Project(Base):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(null=True)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['name']


class E2ECoverage(Base):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False)
    manual = models.PositiveIntegerField(default=0)
    automated = models.PositiveIntegerField(default=0)
    coverage = models.FloatField(default=0)

    def __str__(self):
        return f'"{self.project.name}" project has e2e manual tests = {self.manual} and e2e automated tests = {self.automated}'

    class Meta:
        verbose_name = 'E2E coverage'
        verbose_name_plural = 'E2E coverage'
        ordering = ['project']

    def get_coverage_count(self) -> float:
        try:
            coverage_count = self.automated / (self.manual + self.automated) * 100
        except ZeroDivisionError:
            coverage_count = 0
        return round(coverage_count, 2)


class APICoverage(Base):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False)
    full_coverage = models.FloatField(default=0)
    partial_coverage = models.FloatField(default=0)
    empty_coverage = models.FloatField(default=100)
    actual_cnt = models.PositiveIntegerField(default=0)
    full_cnt = models.PositiveIntegerField(default=0)
    partial_cnt = models.PositiveIntegerField(default=0)
    empty_cnt = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'"{self.project.name}" project has full api coverage {self.full_coverage} {self.full_cnt}/{self.actual_cnt})%'

    class Meta:
        verbose_name = 'API coverage'
        verbose_name_plural = 'API coverage'
        ordering = ['project']


class UnitCoverage(Base):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False)
    code_coverage = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'"{self.project.name}" project has unit tests code coverage = {self.code_coverage}'

    class Meta:
        verbose_name = 'UNIT coverage'
        verbose_name_plural = 'UNIT coverage'
        ordering = ['project']