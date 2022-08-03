from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from shared.models.subjects import SubjectTeacherRelation
from timetable.models.lesson import Lesson


class SubjetcsSerializer(ModelSerializer):
    """Cеарилизация по данныи предмета,аудитории и препода"""

    class Meta:
        model = SubjectTeacherRelation
        fields = [
            'subject_name',
            'teacher',
            'audience',

        ]


class TimetableSerializer(ModelSerializer):
    """Cеарилизация по данныи группа и дня"""

    group = serializers.CharField(source="group.name")

    class Meta:
        model = Lesson
        fields = (
            'group',
            'today_is',
        )

    #
    def to_representation(self, instance):
        """Добавляем уроки на сегодня"""
        representation = super().to_representation(instance)
        representation["today_subjects"] = SubjetcsSerializer(SubjectTeacherRelation.objects.all()[:3],
                                                              many=True).data
        return representation
