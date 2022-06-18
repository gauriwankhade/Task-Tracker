from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from ..validations import TaskValidations
from taskapp.models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView






class TeamViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TeamSerializer

    def create(self, request):
        if request.user.role == 'User':
            serializer = TeamSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "success", "data": serializer.data}, 201)
            return Response(serializer.errors, 400)
        
        return Response({"message": "acccess forbidden"}, 403)


class TaskViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['PATCH'], detail=True)
    def patch(self, request, pk=None):
        instance = Task.objects.get(pk=pk)
        if not TaskValidations.is_user_permitted(request.user.id, 
                                        pk, request.data):
            return Response({"message": "acccess forbidden"}, 403)

        serializer = TaskSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "success", "data": serializer.data}, 200)

    def get(self, request):
        task_objs = Task.objects.all()
        serializer = TaskSerializer(task_objs, many = True)
        return Response({"message": "success", "data": serializer.data}, 200)


    def post(self, request):
        if request.user.role == 'User':
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, 201)
            return Response(serializer.errors, 400)
        
        return Response({"message": "acccess forbidden"}, 403)