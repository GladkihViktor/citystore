# Generated by Django 2.2.4 on 2019-08-18 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20190818_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='name',
            field=models.TextField(default='', max_length=250),
        ),
    ]
