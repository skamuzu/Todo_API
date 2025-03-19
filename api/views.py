from rest_framework.decorators import api_view,authentication_classes,permission_classes
from .models import Task, User
from .serializers import TaskListSerializer, TaskSerializer, RegisterSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

@api_view(["GET","POST"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def task_list(request):
    if request.method == "GET":
        try:
            tasks = Task.objects.filter(user = request.name)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = TaskListSerializer(tasks, many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    elif request.method == "POST":
        serializer = TaskListSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET","PUT","PATCH","DELETE"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def task_item(request,id):
    try:
        task = Task.objects.get(user = request.user, pk = id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = TaskSerializer(task)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        serializer = TaskSerializer(task, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "PATCH":
        serializer = TaskSerializer(task, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
     
@api_view(["POST"]) 
@authentication_classes([])  
@permission_classes([])  
def sign_up(request):
    serializer = RegisterSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)