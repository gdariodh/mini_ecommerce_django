from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.api.serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from users.models import User

class RegisterView(APIView):
    
    # def post -> the post method is customized
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
    def put(self, request):
    
        # get user id from request
        userId = request.user.id
        user = User.objects.get(id=userId)
        serializer = UserUpdateSerializer(user, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)    