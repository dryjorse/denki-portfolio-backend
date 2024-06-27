# Generated by Django 5.0.6 on 2024-06-26 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specializations', '0003_specialization_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialization',
            name='title_en',
            field=models.CharField(max_length=250, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='specialization',
            name='title_es',
            field=models.CharField(max_length=250, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='specialization',
            name='title_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='Название'),
        ),
    ]