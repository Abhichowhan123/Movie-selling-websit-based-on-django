# Generated by Django 3.2.9 on 2021-12-23 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_product_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='detail',
            field=models.CharField(default='', max_length=800, null=True),
        ),
    ]
