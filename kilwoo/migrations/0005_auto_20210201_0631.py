# Generated by Django 3.1.4 on 2021-02-01 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kilwoo', '0004_auto_20210201_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
