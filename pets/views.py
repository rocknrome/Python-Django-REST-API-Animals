from .models import Turtle
from rest_framework import viewsets, permissions
from .serializers import TurtleSerializer
from rest_framework.response import Response
from rest_framework import status

class TurtleViewSet(viewsets.ModelViewSet):
    queryset = Turtle.objects.all().order_by('id')
    serializer_class = TurtleSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
