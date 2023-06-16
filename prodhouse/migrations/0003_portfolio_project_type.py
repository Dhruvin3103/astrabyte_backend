# Generated by Django 4.2.2 on 2023-06-16 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prodhouse', '0002_alter_portfolio_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='project_type',
            field=models.CharField(choices=[('current', 'current projects'), ('past', 'past projects'), ('upcoming', 'upcoming projects')], default='past', max_length=300),
        ),
    ]