# Generated by Django 4.1.1 on 2022-10-03 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='watch',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='watches', to='main_app.brand'),
        ),
    ]
