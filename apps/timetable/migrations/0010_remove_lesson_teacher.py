# Generated by Django 4.0.6 on 2022-08-03 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0009_remove_lesson_teacher_full_name_lesson_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='teacher',
        ),
    ]
