# Generated by Django 4.0.6 on 2022-08-02 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0006_rename_week_day_lesson_today_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='today_subeject',
            new_name='today_subjects',
        ),
    ]
