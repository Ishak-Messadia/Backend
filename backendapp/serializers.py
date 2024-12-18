from rest_framework import serializers
from .models import *


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'  # This will automatically include all fields from the Staff model


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class DossierPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = DossierPatient
        fields = '__all__'
