from django.db import IntegrityError
from django.shortcuts import render
from .serializers import TodoListSerializer
from todo.models import Todos

from rest_framework.generics import ListAPIView
from rest_framework import permissions
from rest_framework.views import csrf_exempt, APIView
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import Http404, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
# Create your views here.

import sys


class TodoListAPIView(ListAPIView):
    serializer_class = TodoListSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        user = self.request.user
        return Todos.objects.filter(user=user).order_by('date')

class TodoCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):

        data = {
            'title':request.data.get('title'),
            'description':request.data.get('description'),
            'user':request.user.id
        }
        
        serializer = TodoListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=200)
        return Response(serializer.errors, status=400)

class TodoUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, id):
        try:
            return Todos.objects.get(id=id)
        except Todos.DoesNotExist:
            return Http404

    def put(self, request, id, *args, **kwargs):

        todo_instance = self.get_object(id)
        if not todo_instance:
            return Response(
                {'error':'Object with todo id does not exist'},
                status=400
            )
        data = {
            'title':request.data.get('title'),
            'description':request.data.get('description'),
            'user':request.user.id
        }

        serializer = TodoListSerializer(todo_instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

class TodoDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, id, request):
        try:
            print(self.request.user.id)
            return Todos.objects.get(id=id, user=request)
            
        except Todos.DoesNotExist:
            return None
            
    def get(self, request, id, *args, **kwargs):
        todo_instance = self.get_object(id, request.user.id)
        
        if not todo_instance:
            return Response({'error':'Object with todo id does not exist'}, status=400)
                
        serializer = TodoListSerializer(todo_instance)
        # if serializer['user'].value == request.user.id:
        #     print('yes')
        return Response(serializer.data, status=200)
        # return Response(status=404)

@api_view(['DELETE'])
def delete(request, id):
    try:
        todo = Todos.objects.get(id=id, user=request.user.id)
    except Todos.DoesNotExist:
        todo = None
    if not todo:
        return JsonResponse({'error':'Object with todo id does not exist'}, status=400)
    todo.delete()
    return JsonResponse({'detail':'Todo deleted succesfully'}, status=200)

@api_view(['POST'])
def complete(request, id):
    try:
        todo = Todos.objects.get(id=id, user=request.user.id)
    except Todos.DoesNotExist:
        todo = None
    if not todo:
        return JsonResponse({'error':'Object with todo id does not exist'}, status=400)
    todo.completed = True
    todo.save()
    print(todo)
    serializer = TodoListSerializer(todo)
    return Response(serializer.data, status=200)
    return JsonResponse({'error':'Something went wrong'})

@csrf_exempt
def signup(request):
    try:

        if request.method == 'POST':

            data = JSONParser().parse(request)
            user = User.objects.create_user(
                username=data['username'],
                password=data['password']
            )
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)}, status=201)
    except IntegrityError:
        return JsonResponse({'error':'username taken, choose another username'}, status=400)

@csrf_exempt
def login (request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(request, username=data['username'], password=data['password'])
        if user is None:
            return JsonResponse({'error':'unable to login, check username and password'}, status=400)
        else:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)}, status=201)


@api_view(['POST'])
def logout(request):
    token = Token.objects.get(user=request.user.id)
    token.delete()
    return JsonResponse({'detail':'User Logged out successfully'}, status=200)