# Generated by Django 4.0.3 on 2022-03-12 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0003_rename_adderss_profile_adderssline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='AdderssLine',
            field=models.CharField(default='', max_length=150),
        ),
    ]
