from django.db import models

from shared.django.models import BaseModel, DeleteModel


class Group(BaseModel, DeleteModel):
    """Модель для хоанения данных о студенте и его группе"""
    name = models.CharField(max_length=50, unique=True)
    students = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('-id',)
