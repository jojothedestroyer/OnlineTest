# Generated by Django 4.2.1 on 2023-05-23 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcna_data', '0005_alter_fullform_date_alter_fullform_inspected_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fullform',
            name='Tree_types',
            field=models.CharField(choices=[('P', 'Nutmeg'), ('C', 'Coconut')], default='A', max_length=50),
        ),
    ]
