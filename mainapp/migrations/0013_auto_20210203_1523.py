# Generated by Django 3.1.5 on 2021-02-03 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_auto_20210203_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproduct',
            name='final_price',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Общая стоимость'),
        ),
    ]
