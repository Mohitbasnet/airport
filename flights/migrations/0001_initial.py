# Generated by Django 4.2.2 on 2023-08-23 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=34)),
                ('destination', models.CharField(max_length=34)),
                ('duration', models.IntegerField()),
            ],
        ),
    ]
