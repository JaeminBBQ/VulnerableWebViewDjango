# Generated by Django 5.0.6 on 2024-05-13 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='app_user',
            name='token',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
