# Generated by Django 2.2.3 on 2019-07-22 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
        ('products', '0004_auto_20190721_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='remove_materials',
            field=models.ManyToManyField(related_name='remove_materials', to='materials.Material'),
        ),
        migrations.AlterField(
            model_name='product',
            name='materials',
            field=models.ManyToManyField(related_name='materials', through='products.ProductMaterial', to='materials.Material'),
        ),
    ]
