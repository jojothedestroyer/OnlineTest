# Generated by Django 4.2.1 on 2023-05-23 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcna_data', '0004_remove_state_annual_production_remove_state_date2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fullform',
            name='date',
            field=models.DateField(null=True, verbose_name='Current Date'),
        ),
        migrations.AlterField(
            model_name='fullform',
            name='inspected_by',
            field=models.DateField(null=True, verbose_name='Inspetion Date'),
        ),
    ]
