# Generated by Django 4.2.1 on 2023-07-25 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcna_data', '0059_rename_sectionu_0_in_house_drying_sectiong_0_fl_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='in_house_drying',
            name='STATION2',
            field=models.CharField(max_length=50, null=True, verbose_name='Station'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='Section',
            field=models.CharField(blank=True, choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='SectionG',
            field=models.CharField(blank=True, choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='SectionGP_1F',
            field=models.CharField(blank=True, choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='SectionGP_2F',
            field=models.CharField(blank=True, choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='SectionGP_FL',
            field=models.CharField(blank=True, choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='SectionGP_GF',
            field=models.CharField(blank=True, choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='SectionG_0_1F',
            field=models.CharField(blank=True, choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='SectionG_0_2F',
            field=models.CharField(blank=True, choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='SectionG_0_FL',
            field=models.CharField(blank=True, choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='SectionG_0_GF',
            field=models.CharField(blank=True, choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='SectionG_1F',
            field=models.CharField(blank=True, choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='SectionG_2F',
            field=models.CharField(blank=True, choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='SectionG_FL',
            field=models.CharField(blank=True, choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='SectionG_GF',
            field=models.CharField(blank=True, choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='SectionH_0_1F',
            field=models.CharField(blank=True, choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='SectionH_0_2F',
            field=models.CharField(blank=True, choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='SectionH_0_FL',
            field=models.CharField(blank=True, choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='SectionH_0_GF',
            field=models.CharField(blank=True, choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='SectionH_1F',
            field=models.CharField(blank=True, choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='SectionH_2F',
            field=models.CharField(blank=True, choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='SectionH_FL',
            field=models.CharField(blank=True, choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='SectionH_GF',
            field=models.CharField(blank=True, choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='SectionM',
            field=models.CharField(blank=True, choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='SectionM_1F',
            field=models.CharField(blank=True, choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='SectionM_2F',
            field=models.CharField(blank=True, choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='SectionM_FL',
            field=models.CharField(blank=True, choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='SectionM_GF',
            field=models.CharField(blank=True, choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='SectionU_1F',
            field=models.CharField(blank=True, choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='SectionU_2F',
            field=models.CharField(blank=True, choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='SectionU_FL',
            field=models.CharField(blank=True, choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='SectionU_GF',
            field=models.CharField(blank=True, choices=[('', '--Select Section--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=50, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='Shelf',
            field=models.CharField(blank=True, choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='ShelfG',
            field=models.CharField(blank=True, choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='ShelfGP_1F',
            field=models.CharField(blank=True, choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='ShelfGP_2F',
            field=models.CharField(blank=True, choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='ShelfGP_FL',
            field=models.CharField(blank=True, choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='ShelfGP_GF',
            field=models.CharField(blank=True, choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='ShelfG_0_1F',
            field=models.CharField(blank=True, choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='ShelfG_0_2F',
            field=models.CharField(blank=True, choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='ShelfG_0_FL',
            field=models.CharField(blank=True, choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='ShelfG_0_GF',
            field=models.CharField(blank=True, choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='ShelfG_1F',
            field=models.CharField(blank=True, choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='ShelfG_2F',
            field=models.CharField(blank=True, choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='ShelfG_FL',
            field=models.CharField(blank=True, choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='ShelfG_GF',
            field=models.CharField(blank=True, choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='ShelfH_0_1F',
            field=models.CharField(blank=True, choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='ShelfH_0_2F',
            field=models.CharField(blank=True, choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='ShelfH_0_FL',
            field=models.CharField(blank=True, choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='ShelfH_0_GF',
            field=models.CharField(blank=True, choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='ShelfH_1F',
            field=models.CharField(blank=True, choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='ShelfH_2F',
            field=models.CharField(blank=True, choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='ShelfH_FL',
            field=models.CharField(blank=True, choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='ShelfH_GF',
            field=models.CharField(blank=True, choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='ShelfM_1F',
            field=models.CharField(blank=True, choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='ShelfM_2F',
            field=models.CharField(blank=True, choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='ShelfM_FL',
            field=models.CharField(blank=True, choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='ShelfM_GF',
            field=models.CharField(blank=True, choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='ShelfU_1F',
            field=models.CharField(blank=True, choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='ShelfU_2F',
            field=models.CharField(blank=True, choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='ShelfU_FL',
            field=models.CharField(blank=True, choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='ShelfU_GF',
            field=models.CharField(blank=True, choices=[('', '--Select shelf--'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L')], max_length=50, null=True, verbose_name='Shelf'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='Tray',
            field=models.CharField(blank=True, choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='TrayG',
            field=models.CharField(blank=True, choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='TrayGP_1F',
            field=models.CharField(blank=True, choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='TrayGP_2F',
            field=models.CharField(blank=True, choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='TrayGP_FL',
            field=models.CharField(blank=True, choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='TrayGP_GF',
            field=models.CharField(blank=True, choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='TrayG_0_1F',
            field=models.CharField(blank=True, choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='TrayG_0_2F',
            field=models.CharField(blank=True, choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='TrayG_0_FL',
            field=models.CharField(blank=True, choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='TrayG_0_GF',
            field=models.CharField(blank=True, choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='TrayG_1F',
            field=models.CharField(blank=True, choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='TrayG_2F',
            field=models.CharField(blank=True, choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='TrayG_FL',
            field=models.CharField(blank=True, choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='TrayG_GF',
            field=models.CharField(blank=True, choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='TrayH_0_1F',
            field=models.CharField(blank=True, choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='TrayH_0_2F',
            field=models.CharField(blank=True, choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='TrayH_0_FL',
            field=models.CharField(blank=True, choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='TrayH_0_GF',
            field=models.CharField(blank=True, choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='TrayH_1F',
            field=models.CharField(blank=True, choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='TrayH_2F',
            field=models.CharField(blank=True, choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='TrayH_FL',
            field=models.CharField(blank=True, choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='TrayH_GF',
            field=models.CharField(blank=True, choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='TrayM_1F',
            field=models.CharField(blank=True, choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='TrayM_2F',
            field=models.CharField(blank=True, choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='TrayM_FL',
            field=models.CharField(blank=True, choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='TrayM_GF',
            field=models.CharField(blank=True, choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='TrayU_1F',
            field=models.CharField(blank=True, choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='TrayU_2F',
            field=models.CharField(blank=True, choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='TrayU_FL',
            field=models.CharField(blank=True, choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
        migrations.AlterField(
            model_name='in_house_drying',
            name='TrayU_GF',
            field=models.CharField(blank=True, choices=[('', '--Select Tray--'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True, verbose_name='Tray'),
        ),
    ]
