# Generated by Django 5.0.6 on 2024-06-24 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='content_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='questions',
            name='content_video',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]