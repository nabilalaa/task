# Generated by Django 3.1.1 on 2020-10-29 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201022_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='meal',
            field=models.CharField(max_length=15, null=1),
            preserve_default=1,
        ),
    ]
