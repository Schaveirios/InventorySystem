# Generated by Django 2.1 on 2018-10-23 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_item_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseditem',
            name='discount',
        ),
    ]