# Generated by Django 5.1.6 on 2025-02-22 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_banner_productattribute'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
    ]
