# Generated by Django 3.2.10 on 2023-07-13 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodapp', '0011_auto_20230713_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestbd',
            name='Hospital',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
