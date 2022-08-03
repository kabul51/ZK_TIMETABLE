from django.db import models
from shared.django.models import BaseModel, DeleteModel



class SubjectTeacherRelation(BaseModel, DeleteModel):
    """Модель для хранения об учителе, предмете и аудитории"""
    room1 = "101"
    room2 = "102"
    room3 = "103"
    room4 = "104"
    room5 = "105"
    room6 = "106"
    room7 = "107"
    room8 = "108"
    room9 = "109"
    room10 = "110"

    AUDIENCE = [
        (room1, '101'),
        (room2, '102'),
        (room3, '103'),
        (room4, '104'),
        (room5, '105'),
        (room6, '106'),
        (room7, '107'),
        (room8, '108'),
        (room9, '109'),
        (room10, '110'),
    ]

    subject_name = models.CharField(max_length=150)
    teacher = models.CharField(max_length=100)
    audience = models.CharField(max_length=150, choices=AUDIENCE, default=room1)


    def __str__(self):
        return f"{self.subject_name,self.teacher}"

