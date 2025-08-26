import django_filters
from .models import Document

class DocumentFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name="name", lookup_expr="icontains", label="Document Name", required=False
    )
    description = django_filters.CharFilter(
        field_name="description", lookup_expr="icontains", label="Description", required=False
    )
    category = django_filters.ChoiceFilter(
        field_name="category",
        choices=Document._meta.get_field("category").choices,
        label="Category",
        required=False
    )
    patient_id = django_filters.NumberFilter(
        field_name="id", 
        label="Patient ID",
        required=False
    )
    created_after = django_filters.DateTimeFilter(
        field_name="created_at", lookup_expr="gte", label="Created After", required=False
    )
    created_before = django_filters.DateTimeFilter(
        field_name="created_at", lookup_expr="lte", label="Created Before", required=False
    )

    class Meta:
        model = Document
        fields = [
            "name",
            "description",
            "category",
            "patient_id",
            "created_after",
            "created_before",
        ]






import django_filters
from .models import Vital, Patient

class VitalFilter(django_filters.FilterSet):
    # Text fields
    vital_type = django_filters.CharFilter(
        field_name="vital_type", lookup_expr="icontains", label="Vital Type", required=False
    )
    unit = django_filters.CharFilter(
        field_name="unit", lookup_expr="icontains", label="Unit", required=False
    )

    # Numeric fields
    value = django_filters.NumberFilter(field_name="value", label="Value", required=False)
    value1 = django_filters.NumberFilter(field_name="value1", label="Value1", required=False)

    # Patient ID filter
    patient_id = django_filters.NumberFilter(field_name="id", label="Patient ID", required=False)

    # Date range filters
    recorded_after = django_filters.DateTimeFilter(
        field_name="recorded_at", lookup_expr="gte", label="Recorded After", required=False
    )
    recorded_before = django_filters.DateTimeFilter(
        field_name="recorded_at", lookup_expr="lte", label="Recorded Before", required=False
    )

    class Meta:
        model = Vital
        fields = [
            "vital_type",
            "unit",
            "value",
            "value1",
            "patient_id",
            "recorded_after",
            "recorded_before",
        ]




import django_filters
from .models import Medication

class MedicationFilter(django_filters.FilterSet):
    medicine = django_filters.CharFilter(
        field_name="medicine", lookup_expr="icontains", label="Medicine", required=False
    )
    type = django_filters.CharFilter(
        field_name="type", lookup_expr="icontains", label="Type", required=False
    )
    sig = django_filters.CharFilter(
        field_name="sig", lookup_expr="icontains", label="SIG", required=False
    )
    qty = django_filters.CharFilter(
        field_name="qty", lookup_expr="icontains", label="Quantity", required=False
    )
    unit = django_filters.CharFilter(
        field_name="unit", lookup_expr="icontains", label="Unit", required=False
    )
    refills = django_filters.CharFilter(
        field_name="refills", lookup_expr="icontains", label="Refills", required=False
    )
    days = django_filters.NumberFilter(
        field_name="days", label="Days", required=False
    )
    patient_id = django_filters.NumberFilter(
        field_name="id", label="Patient ID", required=False
    )
    created_after = django_filters.DateTimeFilter(
        field_name="created_at", lookup_expr="gte", label="Created After", required=False
    )
    created_before = django_filters.DateTimeFilter(
        field_name="created_at", lookup_expr="lte", label="Created Before", required=False
    )

    class Meta:
        model = Medication
        fields = [
            "medicine",
            "type",
            "sig",
            "qty",
            "unit",
            "refills",
            "days",
            "patient_id",
            "created_after",
            "created_before",
        ]
        
        
        
        
        
        
        
        
        
import django_filters
from .models import LabResult

class LabResultFilter(django_filters.FilterSet):
    lab_result_for = django_filters.CharFilter(
        field_name="lab_result_for", lookup_expr="icontains", label="Lab Result For", required=False
    )
    abnormal_flag = django_filters.CharFilter(
        field_name="abnormal_flag", lookup_expr="icontains", label="Abnormal Flag", required=False
    )
    value = django_filters.CharFilter(
        field_name="value", lookup_expr="icontains", label="Value", required=False
    )
    note = django_filters.CharFilter(
        field_name="note", lookup_expr="icontains", label="Note", required=False
    )
    patient_id = django_filters.NumberFilter(
        field_name="id", label="Patient ID", required=False
    )
    file_type = django_filters.CharFilter(
        field_name="file_type", lookup_expr="icontains", label="File Type", required=False
    )
    recorded_after = django_filters.DateTimeFilter(
        field_name="recorded_at", lookup_expr="gte", label="Recorded After", required=False
    )
    recorded_before = django_filters.DateTimeFilter(
        field_name="recorded_at", lookup_expr="lte", label="Recorded Before", required=False
    )

    class Meta:
        model = LabResult
        fields = [
            "lab_result_for",
            "abnormal_flag",
            "value",
            "note",
            "patient_id",
            "file_type",
            "recorded_after",
            "recorded_before",
        ]

