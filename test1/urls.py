from django.urls import path
from myapp.views import Column1FormView, Column2FormView
from django.urls import path
from myapp.views import LabResultsFormView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import PatientViewSet, DocumentViewSet,VitalViewSet, MedicationViewSet,LabResultViewSet

router = DefaultRouter()
router.register(r"patients", PatientViewSet)
router.register(r"documents", DocumentViewSet)
router.register(r"vitals", VitalViewSet)
router.register(r"medications", MedicationViewSet)
router.register(r"lab-results", LabResultViewSet)



urlpatterns = [
    path('column1/', Column1FormView.as_view(), name='column1-form'),
    path('column2/', Column2FormView.as_view(), name='column2-form'),
    path("lab-results/", LabResultsFormView.as_view(), name="lab-results-form"),
    path("api/", include(router.urls)),

    
]