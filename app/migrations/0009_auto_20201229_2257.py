# Generated by Django 3.1.1 on 2020-12-29 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20201229_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='section',
            field=models.CharField(blank=1, max_length=15, null=1),
            preserve_default=1,
        ),
        migrations.AlterField(
            model_name='delivery',
            name='name',
            field=models.CharField(max_length=15, null=1),
        ),
    ]
