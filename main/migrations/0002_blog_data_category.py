# Generated by Django 3.1.4 on 2020-12-31 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_data',
            name='category',
            field=models.CharField(default='', max_length=200),
        ),
    ]
