# Generated by Django 2.2.6 on 2019-11-29 16:03

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20191126_1833'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='My full names')),
                ('picture', models.ImageField(upload_to='')),
                ('hobbies', ckeditor.fields.RichTextField()),
                ('bio', ckeditor.fields.RichTextField()),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
        ),
        migrations.AlterField(
            model_name='learning',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
