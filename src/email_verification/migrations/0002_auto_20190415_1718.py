# Generated by Django 2.2 on 2019-04-15 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_verification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verification',
            name='invite_url',
            field=models.URLField(max_length=2000),
        ),
    ]
