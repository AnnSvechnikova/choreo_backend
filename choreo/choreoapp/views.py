import datetime
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from datetime import date
from rest_framework import viewsets, status, filters
from rest_framework.decorators import api_view, action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from django.db.models import Max, Min
from rest_framework.views import APIView
from choreoapp.serializers import *
from choreoapp.models import Dancer
import uuid
import logging
from rest_framework.generics import get_object_or_404
from importlib import import_module
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.

class DancerViewSet (viewsets.ModelViewSet):
    """api endpoint для просмотра и редактирования списка книг"""
    queryset = Dancer.objects.all()

    def retrieve(self, request, pk=None, **kwargs):
        queryset = Dancer.objects.all()
        d = get_object_or_404(queryset, pk=pk)
        serializer = DancerSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        d = request.data
        d_serialized = DancerSerializer(d)
        d_serialized.save()
        return Response(d_serialized.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None, **kwargs):
        try:
            d = Dancer.objects.get(pk=pk)
        except Dancer.DoesNotExist:
            return Response({'message': 'не существует'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DancerSerializer(d, data=request.data)
        #проверяем, что данные содержат все требуемые поля нужных типов
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None, **kwargs):
        try:
            Dancer.objects.get(pk=pk).delete()
        except Exception:
            return Response(self.serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"status": "ok"}, status=status.HTTP_200_OK)

    