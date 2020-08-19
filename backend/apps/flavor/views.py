from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action

from .serializers import FlavorSerializer, SpectrumSerializer
from .models import Flavor, Spectrum
from .netz import Parse as csvParse


class FlavorViewSet(viewsets.ModelViewSet):
    queryset = Flavor.objects.all()
    serializer_class = FlavorSerializer
    permission_classes = []

    def perform_destroy(self, instance):
        instance.delete()

    @action(detail=True, methods=["post"])
    def set_spectrum(self, request, pk=None):
        flavor = Flavor.objects.get(pk=pk)
        print(flavor)
        print(request.data["spectrum"])
        if request.data.get("spectrum"):
            netz = csvParse(
                request.data.get("spectrum").read().decode("utf-8").splitlines()
            )
            xy = netz.xy()
            meta = netz.meta()
            data = {"meta": meta, "xy": xy}
            spectrum = Spectrum.objects.create(data=data)
            flavor.spectrum = spectrum
            flavor.save()
            return Response(FlavorSerializer(flavor).data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['GET'])
    def get_spectrum(self, request, pk):
        spectrum = Flavor.objects.get(pk=pk).spectrum
        return Response(SpectrumSerializer(spectrum).data)

    @action(detail=False)
    def recent_flavors(self, request):
        recent_flavors = Flavor.objects.all().order_by("-id")
        page = self.paginate_queryset(recent_flavors)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(recent_flavors, many=True)
        return Response(serializer.data)
