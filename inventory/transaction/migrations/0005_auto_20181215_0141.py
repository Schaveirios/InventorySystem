# Generated by Django 2.1.2 on 2018-12-14 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0004_returneditem_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='returneditem',
            name='condition',
            field=models.CharField(max_length=10),
        ),
    ]
