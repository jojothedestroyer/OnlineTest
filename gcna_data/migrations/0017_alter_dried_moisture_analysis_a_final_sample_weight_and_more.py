# Generated by Django 4.2.1 on 2023-05-31 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcna_data', '0016_alter_dried_moisture_analysis_a_date_of_report_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dried_moisture_analysis_a',
            name='Final_Sample_Weight',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=200),
        ),
        migrations.AlterField(
            model_name='dried_moisture_analysis_b',
            name='AVERAGE',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=200),
        ),
        migrations.AlterField(
            model_name='dried_moisture_analysis_b',
            name='Final_Sample_Weight',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=200),
        ),
    ]
