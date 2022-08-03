from django.db import models

from shared.django.models import BaseModel, DeleteModel


class Lesson(BaseModel, DeleteModel):
    """ Модель для хранения групп, дня, уроков на сегодня  """

    MONDAY = 'MONDAY'
    TUESDAY = 'TUESDAY'
    WEDNESDAY = 'WEDNESDAY'
    THURSDAY = 'THURSDAY'
    FRIDAY = 'FRIDAY'
    SATURDAY = 'SATURDAY'

    WEEK_DAYS = [
        (MONDAY, 'monday'),
        (TUESDAY, 'tuesday'),
        (WEDNESDAY, 'wednesday'),
        (THURSDAY, 'thursday'),
        (FRIDAY, 'friday'),
        (SATURDAY, 'saturday'),
    ]

    group = models.ForeignKey("shared.Group", on_delete=models.SET_NULL, null=True, blank=True, related_name='groups')
    today_is = models.CharField(max_length=150, choices=WEEK_DAYS, default=MONDAY)
    today_subjects = models.ForeignKey("shared.SubjectTeacherRelation", on_delete=models.SET_NULL, null=True,
                                       blank=True, related_name='subjectteacherrelations')

    def __str__(self):
        return f"{self.group}"
