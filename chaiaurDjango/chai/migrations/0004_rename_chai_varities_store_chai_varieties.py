# Generated by Django 5.1.3 on 2024-11-25 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0003_chaicertificate_chaireview_store'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='chai_varities',
            new_name='chai_varieties',
        ),
    ]
