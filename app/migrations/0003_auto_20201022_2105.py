# Generated by Django 3.1.1 on 2020-10-22 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20201022_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='name',
            field=models.CharField(max_length=15, null=1),
        ),
    ]
