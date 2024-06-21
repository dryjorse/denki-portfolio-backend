# Generated by Django 5.0.6 on 2024-06-14 16:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
        ('specializations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'verbose_name': 'Навыки', 'verbose_name_plural': 'Навыки'},
        ),
        migrations.AddField(
            model_name='skill',
            name='specialization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='specializations.specialization'),
        ),
    ]