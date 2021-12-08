# Generated by Django 3.2.9 on 2021-12-07 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0017_auto_20211207_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='role',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='role',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Agent', 'Agent'), ('Expense Manager', 'Expense Manager')], default='organisor', max_length=20),
        ),
    ]
