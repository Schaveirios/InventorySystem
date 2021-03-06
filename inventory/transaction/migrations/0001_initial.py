# Generated by Django 2.1 on 2018-10-15 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DefectiveItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Entry Date')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='ImportedStocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Document Date')),
                ('documentNumber', models.PositiveIntegerField()),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('distributor', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('retailPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantityLeft', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='PurchasedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Document Date')),
                ('documentNumber', models.PositiveIntegerField()),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('soldTo', models.CharField(max_length=100)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=4)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transaction.Item')),
            ],
        ),
        migrations.CreateModel(
            name='ReturnedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateReturned', models.DateField(verbose_name='Date Returned')),
                ('remark', models.TextField()),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchasedItem', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transaction.PurchasedItem')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entryDate', models.DateTimeField(verbose_name='Entry Date')),
                ('nameOfTransaction', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='returneditem',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.Transaction'),
        ),
        migrations.AddField(
            model_name='purchaseditem',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.Transaction'),
        ),
        migrations.AddField(
            model_name='importedstocks',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transaction.Item'),
        ),
        migrations.AddField(
            model_name='importedstocks',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.Transaction'),
        ),
        migrations.AddField(
            model_name='defectiveitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transaction.Item'),
        ),
    ]
