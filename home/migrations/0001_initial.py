# Generated by Django 4.1.6 on 2023-02-11 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=255)),
                ('rank', models.CharField(max_length=255)),
                ('country_code', models.CharField(max_length=255)),
                ('points', models.CharField(max_length=255)),
            ],
        ),
    ]
