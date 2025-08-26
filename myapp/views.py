from django.shortcuts import render
from .serializers import column1Serializers, column2Serializers

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

class Column1FormView(GenericAPIView):
    serializer_class = column1Serializers

    def get(self, request):
        serializer = self.get_serializer()
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Column2FormView(GenericAPIView):
    serializer_class = column2Serializers

    def get(self, request):
        serializer = self.get_serializer()
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    



from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import LabResultsSerializer


class LabResultsFormView(GenericAPIView):
    serializer_class = LabResultsSerializer

    def get(self, request):
        """
        Returns an empty schema (field names with default None values)
        so clients know the structure of Lab Results.
        """
        serializer = self.get_serializer()
        return Response(serializer.data)

    def post(self, request):
        """
        Accepts Lab Results JSON (all 83 fields), validates input,
        and returns the validated data or errors.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import Patient, Document, Vital
from .serializers import PatientSerializer, DocumentSerializer, VitalSerializer
from .filters import DocumentFilter, VitalFilter


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["first_name", "last_name", "email"]  # allows ?search=john


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DocumentFilter

# Vital ViewSet
class VitalViewSet(viewsets.ModelViewSet):
    queryset = Vital.objects.all()
    serializer_class = VitalSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = VitalFilter





from .models import Medication
from .serializers import MedicationSerializer
from .filters import MedicationFilter

class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MedicationFilter



from .models import LabResult
from .serializers import LabResultSerializer
from .filters import LabResultFilter

class LabResultViewSet(viewsets.ModelViewSet):
    queryset = LabResult.objects.all()
    serializer_class = LabResultSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LabResultFilter
