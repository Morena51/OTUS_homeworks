# Generated by Django 3.1.4 on 2021-11-30 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_commonswaggercoverage_empty_cnt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commonswaggercoverage',
            name='actual_cnt',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='commonswaggercoverage',
            name='empty_cnt',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='commonswaggercoverage',
            name='full_cnt',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='commonswaggercoverage',
            name='partial_cnt',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
