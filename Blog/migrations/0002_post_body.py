# Generated by Django 4.0.4 on 2022-06-20 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(default='Null'),
            preserve_default=False,
        ),
    ]
