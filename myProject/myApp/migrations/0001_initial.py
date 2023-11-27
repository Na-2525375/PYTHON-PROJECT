# Generated by Django 4.2.7 on 2023-11-27 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authority_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Mobile', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Age', models.CharField(max_length=100)),
                ('myImage', models.ImageField(null=True, upload_to='media/profile_pic')),
            ],
        ),
        migrations.CreateModel(
            name='Employees_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Mobile', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Age', models.CharField(max_length=100)),
                ('myImage', models.ImageField(null=True, upload_to='media/profile_pic')),
            ],
        ),
        migrations.CreateModel(
            name='Library_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_Name', models.CharField(max_length=100)),
                ('Writer_Name', models.CharField(max_length=100)),
                ('Serial_No', models.CharField(max_length=100)),
                ('Acquisition_Date', models.CharField(max_length=100)),
                ('Return_Date', models.CharField(max_length=100)),
                ('myImage', models.ImageField(null=True, upload_to='media/profile_pic')),
            ],
        ),
        migrations.CreateModel(
            name='Students_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Mobile', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Age', models.CharField(max_length=100)),
                ('myImage', models.ImageField(null=True, upload_to='media/profile_pic')),
            ],
        ),
        migrations.CreateModel(
            name='Teachers_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Mobile', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Age', models.CharField(max_length=100)),
                ('myImage', models.ImageField(null=True, upload_to='media/profile_pic')),
            ],
        ),
    ]
