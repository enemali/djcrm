# Generated by Django 3.2.9 on 2021-12-08 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0019_auto_20211208_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
