# Generated by Django 4.2.4 on 2023-09-04 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pHub', '0003_problemi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemi',
            name='nodes',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pHub.nodei'),
        ),
    ]
