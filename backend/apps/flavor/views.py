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
    error = False

    def perform_destroy(self, instance):
        instance.delete()

    @action(detail=True, methods=["post"])
    def spectrum(self, request, pk):
        flavor = Flavor.objects.get(pk=pk)
        if flavor:
            if request.FILES:
                response = {}
                for filename in request.FILES:
                    file = request.FILES[filename]
                    netz = self.spectrum_worker(file.read())
                    pure = self.request.data.get("pure", False)
                    if pure == 'true':
                        pure = True
                    else:
                        pure = False
                    data, bad_data = netz.calculate()
                    if bad_data:
                        response[filename] = status.HTTP_500_INTERNAL_SERVER_ERROR
                        self.error = True
                        continue
                    data["flavor"] = flavor
                    data["pure"] = pure
                    data["file"] = file
                    Spectrum.objects.create(**data)
                    response[filename] = status.HTTP_200_OK
                return Response(response)
            return Response(status=status.HTTP_400_BAD_REQUEST)
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
            Spectrum.objects.values_list(
                "flavor__additive", "flavor__substrate", "ions", named=True
            )
                .filter(ions__isnull=False)
                .filter(pure=True)
                .exclude(ions__exact={})
        )
        serializer = QmidSerializer(qmids, many=True)
        return Response(serializer.data)


class SpectrumViewSet(viewsets.ModelViewSet):
    queryset = Spectrum.objects.all()
    serializer_class = SpectrumSerializer
    permission_classes = []
