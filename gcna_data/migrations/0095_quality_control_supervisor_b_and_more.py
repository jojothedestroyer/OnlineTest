# Generated by Django 4.2.1 on 2023-09-14 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcna_data', '0094_quality_control_supervisor_a'),
    ]

    operations = [
        migrations.AddField(
            model_name='quality_control',
            name='SUPERVISOR_B',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='quality_control',
            name='SUPERVISOR_C',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='quality_control',
            name='SUPERVISOR_D',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='quality_control',
            name='SUPERVISOR_E',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
