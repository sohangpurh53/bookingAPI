# Generated by Django 4.2 on 2023-05-13 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_registration_mobile_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='Mobile_no',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='registration',
            name='Pnr_no',
            field=models.CharField(max_length=10),
        ),
    ]
