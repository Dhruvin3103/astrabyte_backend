# Generated by Django 4.2.2 on 2023-06-16 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodhouse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=models.ImageField(upload_to='image/portfolio/'),
        ),
    ]