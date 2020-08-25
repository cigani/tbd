from rest_framework import serializers
from .models import Flavor, Spectrum


class FlavorSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField()

    class Meta:
        model = Flavor
        fields = "__all__"

    def get_label(self, obj):
        return f"{obj.substrate} - {obj.additive}"

    def update(self, instance, validated_data):
        instance.spectrum = validated_data.get("spectrum", instance.spectrum)
        instance.save()
        return instance


class SubstrateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flavor
        fields = ["substrate"]


class AdditiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flavor
        fields = ["additive"]


class SpectrumSerializer(serializers.ModelSerializer):
    data = serializers.SerializerMethodField()

    class Meta:
        model = Spectrum
        fields = "__all__"

    def get_data(self, obj):
        return obj.data
