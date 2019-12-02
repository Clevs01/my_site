# Generated by Django 2.2.6 on 2019-11-26 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField()),
                ('message', models.TextField()),
                ('recieved_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Learning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='course_pic')),
                ('description', models.TextField()),
            ],
        ),
    ]
