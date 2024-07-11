# Generated by Django 4.1.7 on 2024-02-24 07:06

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('LeelaProject', '0002_rename_suject_contactform_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='diapply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=30)),
                ('email1', models.EmailField(max_length=50)),
                ('phone1', phonenumber_field.modelfields.PhoneNumberField(max_length=20, region=None)),
                ('city', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=10)),
                ('document', models.CharField(max_length=10)),
            ],
        ),
    ]
