# Generated by Django 4.1.5 on 2023-01-25 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicant',
            old_name='cover_later',
            new_name='cover_letter',
        ),
    ]