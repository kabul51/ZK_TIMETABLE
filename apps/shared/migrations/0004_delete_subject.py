# Generated by Django 4.0.6 on 2022-08-03 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0003_subjectteacherrelation'),
        ('timetable', '0008_remove_lesson_today_lesson_today_is_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
