# Generated by Django 4.2.1 on 2023-08-18 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcna_data', '0077_land_info_visit'),
    ]

    operations = [
        migrations.AddField(
            model_name='citrus_mango_trees',
            name='parish',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='citrus_mango_trees',
            name='tenurship',
            field=models.CharField(choices=[('', '--Select an option--'), ('Owned', 'Owned'), ('Freehold', 'Freehold'), ('Leased', 'Leased'), ('Family Land', 'Family Land'), ('ShareCrop', 'ShareCrop'), ('Rent', 'Rent'), ('Rented free', 'Rented free'), ('Premission to work land', 'Premission to work land'), ('Squatted', 'Squatted'), ('Government Land', 'Government Land'), ('Other', 'Other'), ('Caretaker', 'Caretaker'), ('Administrator', 'Administrator')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='citrus_mango_trees',
            name='village',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='coconut_trees',
            name='parish',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='coconut_trees',
            name='tenurship',
            field=models.CharField(choices=[('', '--Select an option--'), ('Owned', 'Owned'), ('Freehold', 'Freehold'), ('Leased', 'Leased'), ('Family Land', 'Family Land'), ('ShareCrop', 'ShareCrop'), ('Rent', 'Rent'), ('Rented free', 'Rented free'), ('Premission to work land', 'Premission to work land'), ('Squatted', 'Squatted'), ('Government Land', 'Government Land'), ('Other', 'Other'), ('Caretaker', 'Caretaker'), ('Administrator', 'Administrator')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='coconut_trees',
            name='village',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='condition',
            name='parish',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='condition',
            name='tenurship',
            field=models.CharField(choices=[('', '--Select an option--'), ('Owned', 'Owned'), ('Freehold', 'Freehold'), ('Leased', 'Leased'), ('Family Land', 'Family Land'), ('ShareCrop', 'ShareCrop'), ('Rent', 'Rent'), ('Rented free', 'Rented free'), ('Premission to work land', 'Premission to work land'), ('Squatted', 'Squatted'), ('Government Land', 'Government Land'), ('Other', 'Other'), ('Caretaker', 'Caretaker'), ('Administrator', 'Administrator')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='condition',
            name='village',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='farm_house',
            name='parish',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='farm_house',
            name='tenurship',
            field=models.CharField(choices=[('', '--Select an option--'), ('Owned', 'Owned'), ('Freehold', 'Freehold'), ('Leased', 'Leased'), ('Family Land', 'Family Land'), ('ShareCrop', 'ShareCrop'), ('Rent', 'Rent'), ('Rented free', 'Rented free'), ('Premission to work land', 'Premission to work land'), ('Squatted', 'Squatted'), ('Government Land', 'Government Land'), ('Other', 'Other'), ('Caretaker', 'Caretaker'), ('Administrator', 'Administrator')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='farm_house',
            name='village',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='farm_water_source',
            name='parish',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='farm_water_source',
            name='tenurship',
            field=models.CharField(choices=[('', '--Select an option--'), ('Owned', 'Owned'), ('Freehold', 'Freehold'), ('Leased', 'Leased'), ('Family Land', 'Family Land'), ('ShareCrop', 'ShareCrop'), ('Rent', 'Rent'), ('Rented free', 'Rented free'), ('Premission to work land', 'Premission to work land'), ('Squatted', 'Squatted'), ('Government Land', 'Government Land'), ('Other', 'Other'), ('Caretaker', 'Caretaker'), ('Administrator', 'Administrator')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='farm_water_source',
            name='village',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='food_safety_and_quality',
            name='parish',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='food_safety_and_quality',
            name='tenurship',
            field=models.CharField(choices=[('', '--Select an option--'), ('Owned', 'Owned'), ('Freehold', 'Freehold'), ('Leased', 'Leased'), ('Family Land', 'Family Land'), ('ShareCrop', 'ShareCrop'), ('Rent', 'Rent'), ('Rented free', 'Rented free'), ('Premission to work land', 'Premission to work land'), ('Squatted', 'Squatted'), ('Government Land', 'Government Land'), ('Other', 'Other'), ('Caretaker', 'Caretaker'), ('Administrator', 'Administrator')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='food_safety_and_quality',
            name='village',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='inspector_symmary',
            name='parish',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='inspector_symmary',
            name='tenurship',
            field=models.CharField(choices=[('', '--Select an option--'), ('Owned', 'Owned'), ('Freehold', 'Freehold'), ('Leased', 'Leased'), ('Family Land', 'Family Land'), ('ShareCrop', 'ShareCrop'), ('Rent', 'Rent'), ('Rented free', 'Rented free'), ('Premission to work land', 'Premission to work land'), ('Squatted', 'Squatted'), ('Government Land', 'Government Land'), ('Other', 'Other'), ('Caretaker', 'Caretaker'), ('Administrator', 'Administrator')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='inspector_symmary',
            name='village',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='land_tenur',
            name='parish',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='land_tenur',
            name='tenurship',
            field=models.CharField(choices=[('', '--Select an option--'), ('Owned', 'Owned'), ('Freehold', 'Freehold'), ('Leased', 'Leased'), ('Family Land', 'Family Land'), ('ShareCrop', 'ShareCrop'), ('Rent', 'Rent'), ('Rented free', 'Rented free'), ('Premission to work land', 'Premission to work land'), ('Squatted', 'Squatted'), ('Government Land', 'Government Land'), ('Other', 'Other'), ('Caretaker', 'Caretaker'), ('Administrator', 'Administrator')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='land_tenur',
            name='village',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='nutmeg_frequency',
            name='parish',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='nutmeg_frequency',
            name='tenurship',
            field=models.CharField(choices=[('', '--Select an option--'), ('Owned', 'Owned'), ('Freehold', 'Freehold'), ('Leased', 'Leased'), ('Family Land', 'Family Land'), ('ShareCrop', 'ShareCrop'), ('Rent', 'Rent'), ('Rented free', 'Rented free'), ('Premission to work land', 'Premission to work land'), ('Squatted', 'Squatted'), ('Government Land', 'Government Land'), ('Other', 'Other'), ('Caretaker', 'Caretaker'), ('Administrator', 'Administrator')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='nutmeg_frequency',
            name='village',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='nutmeg_land',
            name='parish',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='nutmeg_land',
            name='tenurship',
            field=models.CharField(choices=[('', '--Select an option--'), ('Owned', 'Owned'), ('Freehold', 'Freehold'), ('Leased', 'Leased'), ('Family Land', 'Family Land'), ('ShareCrop', 'ShareCrop'), ('Rent', 'Rent'), ('Rented free', 'Rented free'), ('Premission to work land', 'Premission to work land'), ('Squatted', 'Squatted'), ('Government Land', 'Government Land'), ('Other', 'Other'), ('Caretaker', 'Caretaker'), ('Administrator', 'Administrator')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='nutmeg_land',
            name='village',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='nutmeg_trees',
            name='parish',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='nutmeg_trees',
            name='tenurship',
            field=models.CharField(choices=[('', '--Select an option--'), ('Owned', 'Owned'), ('Freehold', 'Freehold'), ('Leased', 'Leased'), ('Family Land', 'Family Land'), ('ShareCrop', 'ShareCrop'), ('Rent', 'Rent'), ('Rented free', 'Rented free'), ('Premission to work land', 'Premission to work land'), ('Squatted', 'Squatted'), ('Government Land', 'Government Land'), ('Other', 'Other'), ('Caretaker', 'Caretaker'), ('Administrator', 'Administrator')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='nutmeg_trees',
            name='village',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='nutmeg_variety',
            name='parish',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='nutmeg_variety',
            name='tenurship',
            field=models.CharField(choices=[('', '--Select an option--'), ('Owned', 'Owned'), ('Freehold', 'Freehold'), ('Leased', 'Leased'), ('Family Land', 'Family Land'), ('ShareCrop', 'ShareCrop'), ('Rent', 'Rent'), ('Rented free', 'Rented free'), ('Premission to work land', 'Premission to work land'), ('Squatted', 'Squatted'), ('Government Land', 'Government Land'), ('Other', 'Other'), ('Caretaker', 'Caretaker'), ('Administrator', 'Administrator')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='nutmeg_variety',
            name='village',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='other_seasoning_trees',
            name='parish',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='other_seasoning_trees',
            name='tenurship',
            field=models.CharField(choices=[('', '--Select an option--'), ('Owned', 'Owned'), ('Freehold', 'Freehold'), ('Leased', 'Leased'), ('Family Land', 'Family Land'), ('ShareCrop', 'ShareCrop'), ('Rent', 'Rent'), ('Rented free', 'Rented free'), ('Premission to work land', 'Premission to work land'), ('Squatted', 'Squatted'), ('Government Land', 'Government Land'), ('Other', 'Other'), ('Caretaker', 'Caretaker'), ('Administrator', 'Administrator')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='other_seasoning_trees',
            name='village',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='other_spices_trees',
            name='parish',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='other_spices_trees',
            name='tenurship',
            field=models.CharField(choices=[('', '--Select an option--'), ('Owned', 'Owned'), ('Freehold', 'Freehold'), ('Leased', 'Leased'), ('Family Land', 'Family Land'), ('ShareCrop', 'ShareCrop'), ('Rent', 'Rent'), ('Rented free', 'Rented free'), ('Premission to work land', 'Premission to work land'), ('Squatted', 'Squatted'), ('Government Land', 'Government Land'), ('Other', 'Other'), ('Caretaker', 'Caretaker'), ('Administrator', 'Administrator')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='other_spices_trees',
            name='village',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='policy',
            name='parish',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='policy',
            name='tenurship',
            field=models.CharField(choices=[('', '--Select an option--'), ('Owned', 'Owned'), ('Freehold', 'Freehold'), ('Leased', 'Leased'), ('Family Land', 'Family Land'), ('ShareCrop', 'ShareCrop'), ('Rent', 'Rent'), ('Rented free', 'Rented free'), ('Premission to work land', 'Premission to work land'), ('Squatted', 'Squatted'), ('Government Land', 'Government Land'), ('Other', 'Other'), ('Caretaker', 'Caretaker'), ('Administrator', 'Administrator')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='policy',
            name='village',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='potential_risks',
            name='parish',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='potential_risks',
            name='tenurship',
            field=models.CharField(choices=[('', '--Select an option--'), ('Owned', 'Owned'), ('Freehold', 'Freehold'), ('Leased', 'Leased'), ('Family Land', 'Family Land'), ('ShareCrop', 'ShareCrop'), ('Rent', 'Rent'), ('Rented free', 'Rented free'), ('Premission to work land', 'Premission to work land'), ('Squatted', 'Squatted'), ('Government Land', 'Government Land'), ('Other', 'Other'), ('Caretaker', 'Caretaker'), ('Administrator', 'Administrator')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='potential_risks',
            name='village',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='road_access',
            name='parish',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='road_access',
            name='tenurship',
            field=models.CharField(choices=[('', '--Select an option--'), ('Owned', 'Owned'), ('Freehold', 'Freehold'), ('Leased', 'Leased'), ('Family Land', 'Family Land'), ('ShareCrop', 'ShareCrop'), ('Rent', 'Rent'), ('Rented free', 'Rented free'), ('Premission to work land', 'Premission to work land'), ('Squatted', 'Squatted'), ('Government Land', 'Government Land'), ('Other', 'Other'), ('Caretaker', 'Caretaker'), ('Administrator', 'Administrator')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='road_access',
            name='village',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
