# Generated by Django 3.1 on 2020-10-23 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=35)),
            ],
        ),
    ]
