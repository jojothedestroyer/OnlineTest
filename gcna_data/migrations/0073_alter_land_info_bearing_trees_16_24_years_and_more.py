# Generated by Django 4.2.1 on 2023-08-17 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcna_data', '0072_alter_land_info_bearing_trees_16_24_years_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='land_info',
            name='Bearing_trees_16_24_years',
            field=models.IntegerField(blank=True, default=0, verbose_name='Estimated production Bearing trees between 16 to 24'),
        ),
        migrations.AlterField(
            model_name='land_info',
            name='Bearing_trees_16_24_years_quantity',
            field=models.IntegerField(blank=True, default=0, verbose_name='Number of Bearing trees between 16 to 24'),
        ),
        migrations.AlterField(
            model_name='land_info',
            name='Bearing_trees_6_15_years_estimated_production',
            field=models.IntegerField(blank=True, default=0, verbose_name='Estimated production Bearing trees between 6 to 14'),
        ),
        migrations.AlterField(
            model_name='land_info',
            name='Bearing_trees_6_15_years_quantity',
            field=models.IntegerField(blank=True, default=0, verbose_name='Number of Bearing trees between 6 to 14'),
        ),
        migrations.AlterField(
            model_name='land_info',
            name='Estimated_peak_period',
            field=models.IntegerField(blank=True, default=0, verbose_name='What is the estimated peak period?'),
        ),
        migrations.AlterField(
            model_name='land_info',
            name='Mature_trees_25_years_estimated_production',
            field=models.IntegerField(default=0, verbose_name='Estimated production for Mature older than 25 years'),
        ),
        migrations.AlterField(
            model_name='land_info',
            name='Mature_trees_25_years_quantity',
            field=models.IntegerField(blank=True, default=0, verbose_name='Number of Mature trees older than 25 years'),
        ),
        migrations.AlterField(
            model_name='land_info',
            name='Non_Bearing_trees_5_years_estimated_production',
            field=models.IntegerField(blank=True, default=0, verbose_name='Estimated production for Non-bearing trees younger than 5 years'),
        ),
        migrations.AlterField(
            model_name='land_info',
            name='Non_Bearing_trees_5_years_quantity',
            field=models.IntegerField(blank=True, default=0, verbose_name='Number of Non-Bearing trees younger than 5 years'),
        ),
    ]
