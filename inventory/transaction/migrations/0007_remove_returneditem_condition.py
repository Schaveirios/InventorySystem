# Generated by Django 2.1 on 2019-01-08 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0006_merge_20181231_0633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='returneditem',
            name='condition',
        ),
    ]