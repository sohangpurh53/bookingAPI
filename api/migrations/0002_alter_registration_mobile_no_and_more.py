# Generated by Django 4.2 on 2023-05-13 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='Mobile_no',
            field=models.SmallIntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='registration',
            name='Pnr_no',
            field=models.SmallIntegerField(max_length=10),
        ),
    ]
