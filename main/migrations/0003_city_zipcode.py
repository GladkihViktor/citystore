# Generated by Django 2.2.4 on 2019-08-14 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_city_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='zipcode',
            field=models.CharField(default='000000', max_length=6, unique=True),
        ),
    ]