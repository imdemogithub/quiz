# Generated by Django 4.0.3 on 2022-03-12 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0002_alter_master_table_alter_profile_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Adderss',
            new_name='AdderssLine',
        ),
    ]
