# Generated by Django 3.1 on 2020-08-31 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='ispasswordmatch',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='passwordcheck',
            field=models.CharField(default='', max_length=255),
        ),
    ]
