# Generated by Django 3.1.4 on 2021-02-15 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kilwoo', '0007_auto_20210215_0433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='caption',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='services',
            name='caption2',
            field=models.TextField(),
        ),
    ]