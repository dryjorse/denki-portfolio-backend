# Generated by Django 5.0.6 on 2024-06-18 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='order',
            field=models.IntegerField(default=1, verbose_name='Место'),
        ),
    ]
