# Generated by Django 5.1.3 on 2024-11-24 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivaraity',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
