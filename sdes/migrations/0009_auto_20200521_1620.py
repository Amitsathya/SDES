# Generated by Django 3.0.4 on 2020-05-21 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdes', '0008_auto_20200521_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='K',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='input',
            name='PT',
            field=models.FloatField(),
        ),
    ]
