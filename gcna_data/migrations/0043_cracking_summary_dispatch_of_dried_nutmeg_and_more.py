# Generated by Django 4.2.1 on 2023-06-29 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcna_data', '0042_alter_other_crops_nutmeg_id_no_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cracking_Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STATION', models.CharField(max_length=50, null=True, verbose_name='Station')),
                ('DATE_OF_CRACKING', models.DateField(null=True, verbose_name='Date of cracking')),
                ('WAREHOUSE_RECEIPT_NUMBERS', models.CharField(max_length=50, null=True, verbose_name='Warehouse Reciept Number')),
                ('NUM_OF_BAGS', models.IntegerField(default=0, verbose_name='Number of Bags')),
                ('LBS_OF_NUTMEGS_CRACKED', models.IntegerField(default=0, verbose_name='Lbs of Nutmegs cracked')),
            ],
        ),
        migrations.CreateModel(
            name='Dispatch_Of_Dried_Nutmeg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STATION', models.CharField(max_length=50, null=True, verbose_name='Station')),
                ('DATE_OF_PICK_UP', models.DateField(null=True, verbose_name='Date of pick up')),
                ('FINAL_MOISTURE_CONTENT', models.IntegerField(default=0, verbose_name='Final moisture content')),
                ('Ground_1', models.IntegerField(default=0, verbose_name='Ground')),
                ('Floor_1st_1', models.IntegerField(default=0, verbose_name='1st Floor')),
                ('Floor_2nd_1', models.IntegerField(default=0, verbose_name='2nd Floor')),
                ('Floor_Loft_1', models.IntegerField(default=0, verbose_name='Loft')),
                ('Ground_2', models.IntegerField(default=0, verbose_name='Ground')),
                ('Floor_1st_2', models.IntegerField(default=0, verbose_name='1st Floor')),
                ('Floor_2nd_2', models.IntegerField(default=0, verbose_name='2nd Floor')),
                ('Floor_Loft_2', models.IntegerField(default=0, verbose_name='Loft')),
                ('BATCH_NUMBER', models.CharField(max_length=50, null=True, verbose_name='Sampling from Gouyvae')),
                ('CORRESPONDING_DELIVERY_ADVICE', models.CharField(max_length=50, null=True, verbose_name='Corresponding Delivery Advice')),
                ('Control_number', models.IntegerField(default=0, verbose_name='Control Number')),
            ],
        ),
        migrations.CreateModel(
            name='Dispatch_Of_Green_Nutmeg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STATION', models.CharField(max_length=50, null=True, verbose_name='Station')),
                ('DATE_OF_PURCHASE', models.DateField(null=True, verbose_name='Date of purchase')),
                ('TOTAL_NUM_OF_FARMERS', models.IntegerField(default=0, verbose_name='Total Numbers of Farmers')),
                ('TOTAL_LBS_NUTMEG_BOUGHT', models.IntegerField(default=0, verbose_name='Total lbs of nutmeg bought')),
                ('NUM_OF_BAGS', models.IntegerField(default=0, verbose_name='Number of Bags')),
                ('DELIVERY_ADVICE_NUMBER', models.CharField(max_length=50, null=True, verbose_name='Delivery  advice Number')),
                ('WAREHOUSE_RECEIPT_NUMBER', models.CharField(max_length=50, null=True, verbose_name='Warehouse Reciept Number')),
                ('CONTROL_NUMBER', models.CharField(max_length=50, null=True, verbose_name='Control Number')),
            ],
        ),
        migrations.CreateModel(
            name='Floation_Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STATION', models.CharField(max_length=50, null=True, verbose_name='Station')),
                ('START_DRYING_DATE', models.DateField(null=True, verbose_name='Start drying date')),
                ('APPROX_END_DRYING_DATE', models.DateField(null=True, verbose_name='Approximate end drying date')),
                ('END_DRYING_DATE', models.DateField(null=True, verbose_name='End drying date')),
                ('Ground_Floor', models.CharField(max_length=50, null=True, verbose_name='Ground Floor')),
                ('Shelf', models.CharField(max_length=50, null=True, verbose_name='Shelf')),
                ('Tray', models.CharField(max_length=50, null=True, verbose_name='Tray')),
                ('FINAL_MOISTURE_H', models.CharField(blank=True, max_length=50, null=True, verbose_name='Heavy Final Moisture')),
                ('FINAL_MOISTURE_L', models.CharField(blank=True, max_length=50, null=True, verbose_name='Light Final Moisture')),
                ('BATCH_NUMBER', models.CharField(max_length=50, null=True, verbose_name='Batch Number')),
            ],
        ),
        migrations.CreateModel(
            name='In_House_Drying',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STATION', models.CharField(max_length=50, null=True, verbose_name='Station')),
                ('DATE_OF_PURCHASE', models.DateField(null=True, verbose_name='Date of Purchase')),
                ('TOTAL_NUM_OF_FARMERS', models.IntegerField(default=0, verbose_name='Total Numbers of Farmers')),
                ('TOTAL_LBS_NUTMEG_BOUGHT', models.IntegerField(default=0, verbose_name='Total lbs of nutmeg bought')),
                ('NUM_OF_BAGS', models.IntegerField(default=0, verbose_name='Number of Bags')),
                ('START_DRYING_DATE', models.DateField(null=True, verbose_name='Start drying date')),
                ('APPROX_END_DRYING_DATE', models.DateField(null=True, verbose_name='Approximate end drying date')),
                ('END_DRYING_DATE', models.DateField(null=True, verbose_name='End drying date')),
                ('Ground_1', models.CharField(max_length=50, null=True, verbose_name='Ground')),
                ('Floor_1st_1', models.CharField(max_length=50, null=True, verbose_name='1st Floor')),
                ('Floor_2nd_1', models.CharField(max_length=50, null=True, verbose_name='2nd Floor')),
                ('Floor_Loft_1', models.CharField(max_length=50, null=True, verbose_name='Loft')),
                ('Ground_2', models.CharField(max_length=50, null=True, verbose_name='Ground')),
                ('Floor_1st_2', models.CharField(max_length=50, null=True, verbose_name='1st Floor')),
                ('Floor_2nd_2', models.CharField(max_length=50, null=True, verbose_name='2nd Floor')),
                ('Floor_Loft_2', models.CharField(max_length=50, null=True, verbose_name='Loft')),
                ('LOCATION3', models.CharField(choices=[('', '--Select Location--'), ('Ground Floor', 'Ground Floor'), ('1st Floor', '1st Floor'), ('2nd Floor', '2nd Floor'), ('Loft', 'Loft')], default='A', max_length=50, verbose_name='Location')),
                ('DEFECT', models.CharField(choices=[('', '--Select Location--'), ('Cracked', 'Cracked'), ('Grow Heads', 'Grow Heads'), ('Lights', 'Lights'), ('Mould', 'Mould')], default='A', max_length=50, verbose_name='Defect')),
                ('PREDOMINANT_DEFECT', models.CharField(choices=[('', '--Select Location--'), ('Cracked', 'Cracked'), ('Grow Heads', 'Grow Heads'), ('Lights', 'Lights'), ('Mould', 'Mould')], default='A', max_length=50, verbose_name='Predominant Defect')),
                ('ALERT', models.CharField(default='A', max_length=50, verbose_name='Defect')),
                ('Sampling_from_gouyvae', models.CharField(max_length=50, null=True, verbose_name='Sampling from Gouyvae')),
                ('Control_number', models.CharField(max_length=50, null=True, verbose_name='Control Number')),
            ],
        ),
        migrations.CreateModel(
            name='Package_Ciontrol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRODUCT_DESCRIPTION', models.CharField(choices=[('', '--Select Description--'), ('SUNS', 'SUNS'), ('GROUND NUTMEG', 'GROUND NUTMEG'), ('CRACKED NUTMEG', 'CRACKED NUTMEG'), (' 110’S MACE', ' 110’S MACE'), (' 80’S MACE', ' 80’S MACE'), ('GUNS', 'GUNS')], default='A', max_length=50, verbose_name='Product Description')),
                ('START', models.DateField(null=True, verbose_name='Start  date')),
                ('END', models.DateField(null=True, verbose_name='End date')),
                ('QUANTITY_OF_BAGS', models.IntegerField(default=0, verbose_name='Quantity of Bags')),
                ('TOTAL_WEIGHT_LBS', models.CharField(max_length=50, null=True, verbose_name='Total weight in lbs')),
                ('PACKAGING_MATERIAL', models.CharField(choices=[('', '--Select Location--'), ('Jute', 'Jute'), ('Polypropylene', 'Polypropylene'), ('Other', 'Other')], default='A', max_length=50, verbose_name='Pakaging Material')),
                ('BATCH_NUMBER', models.CharField(max_length=50, null=True, verbose_name='Batch Number')),
                ('CONTRACT_NUMBER', models.CharField(max_length=50, null=True, verbose_name='Contract Shipment Number')),
                ('OFFICIAL_LAB_RESULTS', models.CharField(max_length=50, null=True, verbose_name='Official Lab Results')),
            ],
        ),
    ]
