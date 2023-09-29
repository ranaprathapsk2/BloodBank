# Generated by Django 3.2.10 on 2023-08-21 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodapp', '0022_articledb_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('Subject', models.CharField(blank=True, max_length=200, null=True)),
                ('Message', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
