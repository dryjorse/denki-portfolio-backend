# Generated by Django 5.0.6 on 2024-06-14 16:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('skills', '0002_alter_skill_options_skill_specialization'),
        ('specializations', '0002_alter_specialization_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('date', models.DateField(verbose_name='Дата завершения')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='images/projects')),
                ('skills', models.ManyToManyField(to='skills.skill')),
                ('specialization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='specializations.specialization')),
            ],
        ),
    ]