# Generated by Django 3.0.6 on 2020-10-27 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200514_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
