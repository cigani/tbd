from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action

from .serializers import (
    FlavorSerializer,
    SpectrumSerializer,
    SubstrateSerializer,
    AdditiveSerializer,
    QmidSerializer,
)
from .models import Flavor, Spectrum
from .netz import Parse as csvParse


class FlavorViewSet(viewsets.ModelViewSet):
    queryset = Flavor.objects.all()
    serializer_class = FlavorSerializer
    permission_classes = []
    spectrum_worker = csvParse

    def perform_destroy(self, instance):
        instance.delete()

    @action(detail=True, methods=["post"])
    def spectrum(self, request, pk):
        flavor = Flavor.objects.get(pk=pk)
        print(request.data, flavor, pk)
        if request.data.get("file"):
            file = request.data.get("file")
            netz = self.spectrum_worker(file.read())
            pure = self.request.data.get('pure', False)
            data = netz.calculte()
            data['flavor'] = flavor
            data['pure'] = pure
            data['file'] = file
            spectrum = Spectrum.objects.create(**data)
            # serializer = FlavorSerializer(flavor, data=data)
            # serializer.is_valid(raise_exception=True)
            # serializer.save()
            return Response(SpectrumSerializer(spectrum).data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @action(detail=False)
    def substrates(self, request):
        substrates = (
            Flavor.objects.values_list("substrate", named=True)
                .distinct("substrate")
                .exclude(substrate__isnull=True)
        )
        serializer = SubstrateSerializer(substrates, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def additives(self, request):
        additives = (
            Flavor.objects.values_list("additive", named=True)
                .distinct("additive")
                .exclude(additive__isnull=True)
        )
        serializer = AdditiveSerializer(additives, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def qmids(self, request):
        qmids = (
            Spectrum.objects.values_list("flavor__additive", "ions", named=True)
                .filter(ions__isnull=False)
                .exclude(ions__exact={})
        )
        serializer = QmidSerializer(qmids, many=True)
        return Response(serializer.data)


class SpectrumViewSet(viewsets.ModelViewSet):
    queryset = Spectrum.objects.all()
    serializer_class = SpectrumSerializer
    permission_classes = []
