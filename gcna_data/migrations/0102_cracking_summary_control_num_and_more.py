# Generated by Django 4.2.1 on 2023-09-27 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcna_data', '0101_quality_control_assortor6_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cracking_summary',
            name='Control_Num',
            field=models.IntegerField(default=0, verbose_name='Number of Bags'),
        ),
        migrations.AddField(
            model_name='cracking_summary',
            name='Delivery_Advice_Num',
            field=models.IntegerField(default=0, verbose_name='Number of Bags'),
        ),
        migrations.AddField(
            model_name='floation_summary',
            name='Control_NUMBER',
            field=models.CharField(max_length=50, null=True, verbose_name='Batch Number'),
        ),
        migrations.AlterField(
            model_name='cracking_summary',
            name='STATION',
            field=models.CharField(choices=[('', '--Select Location--'), ('H', 'Beaulieu'), ('M', 'Gouyave'), ('G', 'Grenville')], max_length=50, null=True, verbose_name='Station'),
        ),
        migrations.AlterField(
            model_name='dispatch_of_green_nutmeg',
            name='STATION',
            field=models.CharField(choices=[('', '--Select Location--'), ('G', 'Grenville'), ('H', 'Hermitage'), ('M', 'Marli'), ('U', 'Union'), ('GP', 'Gouyave'), ('V', 'Victoria')], max_length=50, null=True, verbose_name='Station'),
        ),
    ]