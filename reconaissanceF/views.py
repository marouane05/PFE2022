from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Person
from .serializers import PersonSerializer
# Create your views here.
class PersonListApiView(APIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]
    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        """todos = Todo.objects.filter(user = request.user.id)
        """
        Persons = Person.objects.filter();
        serializer = PersonSerializer(Persons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):

        data = {
            'nom' : request.data.get('nom'),
            'prenom':request.data.get('prenom'),
            'role': request.data.get('role'),
            'image':request.data.get('image')
        }

        serializer = PersonSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)