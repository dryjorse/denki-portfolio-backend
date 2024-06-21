# Generated by Django 5.0.6 on 2024-06-14 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0003_remove_skill_specialization'),
        ('specializations', '0002_alter_specialization_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialization',
            name='skills',
            field=models.ManyToManyField(to='skills.skill'),
        ),
    ]
