# Generated by Django 4.0.6 on 2022-08-02 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='subeject',
            new_name='subeject_name',
        ),
    ]
