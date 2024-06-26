# Generated by Django 5.0.6 on 2024-06-26 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='project',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='project',
            name='title_en',
            field=models.CharField(max_length=250, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='project',
            name='title_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='Название'),
        ),
    ]
