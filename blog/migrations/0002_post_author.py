# Generated by Django 5.1.7 on 2025-03-12 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='Anonymous', max_length=100),
        ),
    ]
