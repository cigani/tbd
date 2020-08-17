from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action

from .serializers import FlavorSerializer
from .models import Flavor
import csv

class FlavorViewSet(viewsets.ModelViewSet):
    queryset = Flavor.objects.all()
    serializer_class = FlavorSerializer
    permission_classes = []

    def perform_destroy(self, instance):
        instance.delete()

    @action(detail=True, methods=['post'])
    def set_spectrum(self, request, pk=None):
        flavor = Flavor.objects.get(pk=pk)
        print(flavor)
        print(request.data['spectrum'])
        print(pk)
        serializer=self.get_serializer()
        return Response(serializer.data)
    @action(detail=False)
    def recent_flavors(self, request):
        recent_flavors = Flavor.objects.all().order_by("-id")
        page = self.paginate_queryset(recent_flavors)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_flavors, many=True)
        return Response(serializer.data)
