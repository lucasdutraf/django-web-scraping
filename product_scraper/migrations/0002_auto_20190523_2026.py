# Generated by Django 2.2.1 on 2019-05-23 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_scraper', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='Product',
            old_name='idProduct',
            new_name='id',
        ),
    ]
