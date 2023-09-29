# Generated by Django 3.2.10 on 2023-07-11 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodapp', '0007_requestbd_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerdb',
            name='Age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='registerdb',
            name='District',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='registerdb',
            name='Gender',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='registerdb',
            name='LastName',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='registerdb',
            name='MobileNumber',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='registerdb',
            name='Place',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='registerdb',
            name='RePassword',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
