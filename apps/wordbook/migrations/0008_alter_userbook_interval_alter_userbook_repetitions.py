# Generated by Django 4.0.4 on 2022-04-29 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordbook', '0007_alter_userbook_interval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbook',
            name='interval',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userbook',
            name='repetitions',
            field=models.IntegerField(default=0),
        ),
    ]
