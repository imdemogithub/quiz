# Generated by Django 4.0.3 on 2022-03-24 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0006_alter_category_options_quesset_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='master',
            name='LastLogin',
        ),
        migrations.AddField(
            model_name='master',
            name='LastUpdated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='master',
            name='DateCreated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
