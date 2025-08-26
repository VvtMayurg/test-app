from django.db import models
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Patient(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


DOCUMENT_CATEGORY_CHOICES = [
    ("lab", "Lab Report"),
    ("prescription", "Prescription"),
    ("imaging", "Imaging"),
]

class Document(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="documents")
    category = models.CharField(max_length=50, choices=DOCUMENT_CATEGORY_CHOICES)
    file = models.FileField(upload_to="documents/", blank=True, null=True)

    def __str__(self):
        return self.name


class Vital(BaseModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="vitals")
    vital_type = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=6, decimal_places=2)
    value1 = models.DecimalField(max_digits=6, decimal_places=2)
    unit = models.CharField(max_length=50)
    recorded_at = models.DateTimeField()
    metadata = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.vital_type} for {self.patient}"


class Medication(BaseModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="medications")
    medicine = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    sig = models.CharField(max_length=255)
    qty = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    refills = models.CharField(max_length=255)
    days = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.medicine} for {self.patient}"



class LabResult(BaseModel):
    lab_result_for = models.CharField(max_length=255)
    abnormal_flag = models.CharField(max_length=255, null=True, blank=True)
    value = models.CharField(max_length=255, blank=True)
    note = models.TextField(null=True, blank=True)
    recorded_at = models.DateTimeField(null=True, blank=True)
    file = models.FileField(upload_to="lab_results/", null=True, blank=True)
    file_type = models.CharField(max_length=50, null=True, blank=True)
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="lab_results",
    )

    def __str__(self):
        return f"{self.lab_result_for} for {self.patient}"
