from rest_framework import serializers
from .models import Flavor, Spectrum


class FlavorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flavor
        fields = "__all__"


class SpectrumSerializer(serializers.ModelSerializer):
    data = serializers.SerializerMethodField()

    class Meta:
        model = Spectrum
        fields = ["id", "data"]

    def get_data(self, obj):
        return obj.data
