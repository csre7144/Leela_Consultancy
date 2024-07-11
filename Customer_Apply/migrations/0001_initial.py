# Generated by Django 4.1.7 on 2024-02-27 07:14

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data_Engineer_apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name2', models.CharField(max_length=30)),
                ('email2', models.EmailField(max_length=50)),
                ('phone2', phonenumber_field.modelfields.PhoneNumberField(max_length=20, region=None)),
                ('city2', models.CharField(max_length=30)),
                ('document2', models.FileField(upload_to='Resume/')),
            ],
        ),
        migrations.CreateModel(
            name='Data_Integration_Engineer_Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=30)),
                ('email1', models.EmailField(max_length=50)),
                ('phone1', phonenumber_field.modelfields.PhoneNumberField(max_length=20, region=None)),
                ('city', models.CharField(max_length=30)),
                ('document', models.FileField(upload_to='Resume/')),
            ],
        ),
        migrations.CreateModel(
            name='Informatica_Programmer_Analyst_Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name2', models.CharField(max_length=30)),
                ('email2', models.EmailField(max_length=50)),
                ('phone2', phonenumber_field.modelfields.PhoneNumberField(max_length=20, region=None)),
                ('city2', models.CharField(max_length=30)),
                ('document2', models.FileField(upload_to='Resume/')),
            ],
        ),
        migrations.CreateModel(
            name='Intern_Etl_Developer_Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name2', models.CharField(max_length=30)),
                ('email2', models.EmailField(max_length=50)),
                ('phone2', phonenumber_field.modelfields.PhoneNumberField(max_length=20, region=None)),
                ('city2', models.CharField(max_length=30)),
                ('document2', models.FileField(upload_to='Resume/')),
            ],
        ),
        migrations.CreateModel(
            name='IT_Internship_Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name2', models.CharField(max_length=30)),
                ('email2', models.EmailField(max_length=50)),
                ('phone2', phonenumber_field.modelfields.PhoneNumberField(max_length=20, region=None)),
                ('city2', models.CharField(max_length=30)),
                ('document2', models.FileField(upload_to='Resume/')),
            ],
        ),
        migrations.CreateModel(
            name='Solutions_Architect_Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name2', models.CharField(max_length=30)),
                ('email2', models.EmailField(max_length=50)),
                ('phone2', phonenumber_field.modelfields.PhoneNumberField(max_length=20, region=None)),
                ('city2', models.CharField(max_length=30)),
                ('document2', models.FileField(upload_to='Resume/')),
            ],
        ),
        migrations.CreateModel(
            name='Sr_Data_Architect_Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name2', models.CharField(max_length=30)),
                ('email2', models.EmailField(max_length=50)),
                ('phone2', phonenumber_field.modelfields.PhoneNumberField(max_length=20, region=None)),
                ('city2', models.CharField(max_length=30)),
                ('document2', models.FileField(upload_to='Resume/')),
            ],
        ),
    ]
