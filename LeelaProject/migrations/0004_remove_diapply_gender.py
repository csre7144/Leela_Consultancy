# Generated by Django 4.1.7 on 2024-02-24 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LeelaProject', '0003_diapply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diapply',
            name='gender',
        ),
    ]
