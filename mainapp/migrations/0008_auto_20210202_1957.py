# Generated by Django 3.1.5 on 2021-02-02 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20210130_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='sd',
            field=models.BooleanField(default=False, verbose_name='Наличие cd карты'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='sd_volume',
            field=models.IntegerField(blank=True, max_length=255, null=True, verbose_name='Объём памяти'),
        ),
    ]
