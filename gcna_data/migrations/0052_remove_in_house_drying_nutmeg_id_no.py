# Generated by Django 4.2.1 on 2023-07-07 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gcna_data', '0051_remove_in_house_drying_worker_id_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='in_house_drying',
            name='Nutmeg_ID_No',
        ),
    ]
