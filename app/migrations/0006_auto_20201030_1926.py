# Generated by Django 3.1.1 on 2020-10-30 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201030_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='name',
            field=models.CharField(blank=1, default='nabil', max_length=15, null=1),
        ),
    ]
