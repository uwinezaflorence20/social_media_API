from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegisterSerializer

@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User registered successfully"}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    from django.contrib.auth import authenticate
    user = authenticate(username=username, password=password)
    if user:
        return Response({"message": "Login successful"})
    return Response({"error": "Invalid credentials"}, status=400)

@api_view(['GET'])
def get_all_users(request):
    users = User.objects.all()
    serializer = RegisterSerializer(users, many=True)
    # Don't return passwords
    for user_data in serializer.data:
        user_data.pop('password', None)
    return Response(serializer.data)
