# Generated by Django 4.1.1 on 2022-10-03 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_watch_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='watch',
            name='jm_owns',
            field=models.BooleanField(default=False),
        ),
    ]
