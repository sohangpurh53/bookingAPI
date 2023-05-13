# Generated by Django 4.2 on 2023-05-13 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=100)),
                ('Last_name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Mobile_no', models.IntegerField(max_length=10)),
                ('Pnr_no', models.BigIntegerField(max_length=10)),
                ('Date', models.DateTimeField()),
            ],
        ),
    ]
