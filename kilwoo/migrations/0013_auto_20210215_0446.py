# Generated by Django 3.1.4 on 2021-02-15 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kilwoo', '0012_auto_20210215_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='caption2',
            field=models.TextField(blank=True, null=True),
        ),
    ]
