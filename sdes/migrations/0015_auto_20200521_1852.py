# Generated by Django 3.0.4 on 2020-05-21 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdes', '0014_auto_20200521_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='E',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='input',
            name='IP',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='input',
            name='IPi',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='input',
            name='O',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='input',
            name='P4',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='input',
            name='P8',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='input',
            name='S0',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='input',
            name='S1',
            field=models.FloatField(default=None),
        ),
    ]