# Generated by Django 4.0.1 on 2022-01-28 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier_integration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='couriers',
            name='waybillID',
            field=models.CharField(max_length=100),
        ),
    ]
