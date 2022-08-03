from django.db import models

from shared.django.models import BaseModel, DeleteModel


class Role(BaseModel, DeleteModel):
    "Распределение ролей "
    ROLE_CHOICES = (
        ("admin", "admin"),
        ("student", "student"),
        ("teacher", "teacher"),
    )

    unique_name = models.CharField(max_length=255, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.unique_name}"
