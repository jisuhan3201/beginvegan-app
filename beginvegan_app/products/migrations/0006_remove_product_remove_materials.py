# Generated by Django 2.2.3 on 2019-07-22 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20190722_1022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='remove_materials',
        ),
    ]
