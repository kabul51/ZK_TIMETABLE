from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from timetable.models.lesson import Lesson
from timetable.serializers.timetable import TimetableSerializer


class ListLessonView(ListAPIView):
    """ Выводим расписание уроков """
    queryset = Lesson.objects.all()
    serializer_class = TimetableSerializer
    permission_classes = [IsAuthenticated]
