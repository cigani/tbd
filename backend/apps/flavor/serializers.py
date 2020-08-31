from rest_framework import serializers
from .models import Flavor, Spectrum
from drf_dynamic_fields import DynamicFieldsMixin


class QmidSerializer(serializers.ModelSerializer):
    qmids = serializers.SerializerMethodField()

    class Meta:
        model = Flavor
        fields = ['qmids']

    def get_qmids(self, obj):
        if (obj.flavor__additive and obj.flavor__substrate):
            return {f"{obj.flavor__substrate} - {obj.flavor__additive}": obj.ions}
        elif (obj.flavor__additive):
            return {obj.flavor__additive: obj.ions}
        else:
            return {obj.flavor__substrate: obj.ions}

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        profile_representation = representation.pop("qmids")
        return profile_representation


class SubstrateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flavor
        fields = ["substrate"]


class AdditiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flavor
        fields = ["additive"]


class SpectrumSerializer(DynamicFieldsMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Spectrum
        fields = ('id', 'meta', 'ions', 'file', 'pure', 'data', 'formulation')


class FlavorSerializer(serializers.ModelSerializer):
    label = serializers.SerializerMethodField()
    meta = serializers.SerializerMethodField()
    class Meta:
        model = Flavor
        fields = ['id', 'substrate', 'additive', 'notes', 'label', 'spectrum', 'meta']

    def get_label(self, obj):
        return f"{obj.substrate} - {obj.additive}"

    def get_meta(self, obj):
        return obj.spectrum.values_list('meta', named=True)
