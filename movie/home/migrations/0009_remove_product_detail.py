# Generated by Django 3.2.9 on 2021-12-23 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_product_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='detail',
        ),
    ]
