from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from trainee.models import Trainee
from course.models import Course
from trainee.serializers import TraineeSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class TraineeViewSet(ModelViewSet):
    queryset = Trainee.objects.filter(isactive=True)
    serializer_class = TraineeSerializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        print("Received Data:", request.data)

        trname = request.data.get('name')
        tremail = request.data.get('email')
        trage = request.data.get('age')
        trimg = request.FILES.get('image')
        trcourse_id = request.data.get('course')
        trdate = request.data.get('joined_date')

        trcourse = get_object_or_404(Course, id=trcourse_id)
        trainee = Trainee.objects.create(
            name=trname,
            email=tremail,
            age=trage,
            image=trimg,
            course=trcourse,
            joined_date=trdate
        )

        serializer = self.get_serializer(trainee)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        trainee = self.get_object()
        data = request.data.copy()

        if "trimg" in request.FILES:
            data["image"] = request.FILES["trimg"]

        if "trcourse" in data:
            course = get_object_or_404(Course, id=data["trcourse"])
            data["course"] = course.id

        serializer = self.get_serializer(trainee, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        trainee = self.get_object()
        trainee.isactive = False
        trainee.save()
        return Response({"message": "Trainee deactivated successfully."}, status=status.HTTP_204_NO_CONTENT)
