# Generated by Django 2.2.3 on 2019-07-22 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
        ('products', '0006_remove_product_remove_materials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmaterial',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pm_material', to='materials.Material'),
        ),
        migrations.AlterField(
            model_name='productmaterial',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pm_product', to='products.Product'),
        ),
        migrations.CreateModel(
            name='RemoveMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rm_material', to='materials.Material')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rm_product', to='products.Product')),
            ],
            options={
                'db_table': 'remove_material',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='remove_materials',
            field=models.ManyToManyField(related_name='remove_materials', through='products.RemoveMaterial', to='materials.Material'),
        ),
    ]
