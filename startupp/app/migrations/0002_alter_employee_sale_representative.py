# Generated by Django 4.0.6 on 2022-10-09 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Sale_Representative',
            field=models.DateTimeField(max_length=40),
        ),
    ]
