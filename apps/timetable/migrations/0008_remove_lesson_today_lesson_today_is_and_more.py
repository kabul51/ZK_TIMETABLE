# Generated by Django 4.0.6 on 2022-08-03 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0003_subjectteacherrelation'),
        ('timetable', '0007_rename_today_subeject_lesson_today_subjects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='today',
        ),
        migrations.AddField(
            model_name='lesson',
            name='today_is',
            field=models.CharField(choices=[('MONDAY', 'monday'), ('TUESDAY', 'tuesday'), ('WEDNESDAY', 'wednesday'), ('THURSDAY', 'thursday'), ('FRIDAY', 'friday'), ('SATURDAY', 'saturday')], default='MONDAY', max_length=150),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='today_subjects',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subjectteacherrelations', to='shared.subjectteacherrelation'),
        ),
    ]