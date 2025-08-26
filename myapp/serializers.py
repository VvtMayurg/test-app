
from rest_framework import serializers
class column1Serializers(serializers.Serializer):
    created_at = serializers.DateTimeField(read_only=True)
    
    NOTE_CHOICES = [
        ('Office-note', 'Office-note'),
        ('progress-note', 'progress-note'),
        ('followup-note', 'followup-note'),
    ]
    DOCTOR_CHOICES=[
        
        ('Dr.James JOne','Dr.James JOne'),
        ('Dr.Smith','Dr.Smith'),
        ('Dr.Emily','Dr.Emily'),
    ]
    
    note = serializers.ChoiceField(choices=NOTE_CHOICES)
    doctor_name = serializers.ChoiceField(choices=DOCTOR_CHOICES)
    time_with_patients = serializers.DurationField()
    exam_reason = serializers.CharField()
    allergies = serializers.CharField(max_length=255, allow_blank=True)
    past_medical_history = serializers.CharField(max_length=255, allow_blank=True)
    past_surgical_history = serializers.CharField(max_length=255, allow_blank=True)
    family_history = serializers.CharField(allow_blank=True)
    social_history = serializers.CharField(allow_blank=True)
    habits = serializers.CharField(allow_blank=True)
    current_medication = serializers.CharField(allow_blank=True)
    review_of_system = serializers.CharField(allow_blank=True)
    followup = serializers.CharField(allow_blank=True)
    transition_of_care = serializers.BooleanField(default=False)
    received_from_other_setting_or_provider = serializers.BooleanField(default=False)
    referring_to_other_setting_or_provider = serializers.BooleanField(default=False)
    keep_this_confidential = serializers.BooleanField(default=False)


class column2Serializers(serializers.Serializer):
    created_at = serializers.DateTimeField(read_only=True)

    NOTE_CHOICES = [
        ('Office-note', 'Office-note'),
        ('progress-note', 'progress-note'),
        ('followup-note', 'followup-note'),
    ]
    
    DOCTOR_CHOICES = [
        ('Dr.James JOne', 'Dr.James JOne'),
        ('Dr.Smith', 'Dr.Smith'),
        ('Dr.Emily', 'Dr.Emily'),
    ]

    note = serializers.ChoiceField(choices=NOTE_CHOICES)
    doctor_name = serializers.ChoiceField(choices=DOCTOR_CHOICES)
    time_with_patients = serializers.DurationField()
    allergies = serializers.CharField(max_length=255, allow_blank=True)
    past_medical_history = serializers.CharField(max_length=255, allow_blank=True)
    past_surgical_history = serializers.CharField(max_length=255, allow_blank=True)
    family_history = serializers.CharField(allow_blank=True)
    social_history = serializers.CharField(allow_blank=True)
    habits = serializers.CharField(allow_blank=True)
    current_medication = serializers.CharField(allow_blank=True)
    review_of_system = serializers.CharField(allow_blank=True)
    followup = serializers.CharField(allow_blank=True)
    transition_of_care = serializers.BooleanField(required=False, default=False)
    received_from_other_setting_or_provider = serializers.BooleanField(required=False, default=False)
    referring_to_other_setting_or_provider = serializers.BooleanField(required=False, default=False)
    keep_this_confidential = serializers.BooleanField(default=False)




class LabResultsSerializer(serializers.Serializer):
    collected = serializers.DateField(required=False)
    resulted = serializers.DateField(required=False)
    hematocrit = serializers.FloatField(required=False)       
    hemoglobin = serializers.FloatField(required=False)       
    mcv = serializers.FloatField(required=False)              
    platelates = serializers.FloatField(required=False)
    rbc = serializers.FloatField(required=False)
    wbc = serializers.FloatField(required=False)
    a_g_ratio = serializers.FloatField(required=False)
    albumin = serializers.FloatField(required=False)
    alkaline_phosphatase = serializers.FloatField(required=False)
    alt = serializers.FloatField(required=False)
    ast = serializers.FloatField(required=False)
    bilirubin_total = serializers.FloatField(required=False)
    bun = serializers.FloatField(required=False)
    bun_creatinine_ratio = serializers.FloatField(required=False)
    calcium = serializers.FloatField(required=False)
    carbon_dioxide = serializers.FloatField(required=False)
    chloride = serializers.FloatField(required=False)
    creatinine = serializers.FloatField(required=False)
    egfr = serializers.FloatField(required=False)
    globulin = serializers.FloatField(required=False)
    glucose = serializers.FloatField(required=False)
    potassium = serializers.FloatField(required=False)
    protein = serializers.FloatField(required=False)
    sodium = serializers.FloatField(required=False)
    sars_cov_2_igg = serializers.FloatField(required=False)
    sars_cov_2_assay = serializers.FloatField(required=False)
    architect_sars_cov_2_igg = serializers.FloatField(required=False)
    abbott_real_time_sars_cov_2 = serializers.FloatField(required=False)
    abbott_id_now_covid_19 = serializers.FloatField(required=False)
    carestart_covid_19 = serializers.FloatField(required=False)
    bd_veritor_sars_cov_2 = serializers.FloatField(required=False)
    bio_rad_platelia_total = serializers.FloatField(required=False)
    biofire_covid_19_test = serializers.FloatField(required=False)
    biomerieux_argene_sars_cov_2r_gene = serializers.FloatField(required=False)
    biomerieux_vidas_sars_cov_2_igg = serializers.FloatField(required=False)
    biomerieux_vidas_sars_cov_2_igm = serializers.FloatField(required=False)
    cepheid_xpert_xpress_sars_cov_2 = serializers.FloatField(required=False)
    diasorin_liaison_sars_cov_2_s1s2_igg = serializers.FloatField(required=False)
    diasorin_molecular_simplexa_covid_19_direct = serializers.FloatField(required=False)
    genmark_dx_eplex_sars_cov_2_test = serializers.FloatField(required=False)
    healgen_scientific_covid_19_igg_rapid_test = serializers.FloatField(required=False)
    healgen_scientific_covid_19_igm_rapid_test = serializers.FloatField(required=False)
    hologic_panther_fusion_sars_cov_2 = serializers.FloatField(required=False)
    luminex_aries_sars_cov_2_assay = serializers.FloatField(required=False)
    luminex_nxtag_cov = serializers.FloatField(required=False)
    mesa_biotech_accula_sars_cov_2 = serializers.FloatField(required=False)
    quidel_lyra_sars_cov_2_assay = serializers.FloatField(required=False)
    quidel_sofia_2_sars_antigen_fluorescent = serializers.FloatField(required=False)
    fit_ifobt = serializers.FloatField(required=False)
    fit_dna = serializers.FloatField(required=False)
    fobt = serializers.FloatField(required=False)
    glucose1 = serializers.FloatField(required=False)  
    hemoglobin_a1c = serializers.FloatField(required=False)
    cholesterol_total = serializers.FloatField(required=False)
    hdl_cholesterol = serializers.FloatField(required=False)
    ldl_cholesterol = serializers.FloatField(required=False)
    triglycerides = serializers.FloatField(required=False)
    microalbumin = serializers.FloatField(required=False)
    urine_hcg = serializers.FloatField(required=False)
    psa = serializers.FloatField(required=False)
    inr = serializers.FloatField(required=False)
    prothrombin_time = serializers.FloatField(required=False)
    rapid_hiv = serializers.FloatField(required=False)
    rapid_influenza_a = serializers.FloatField(required=False)
    rapid_influenza_b = serializers.FloatField(required=False)
    monospot = serializers.FloatField(required=False)
    rapid_step_a = serializers.FloatField(required=False)
    induration = serializers.FloatField(required=False)
    tb = serializers.FloatField(required=False)
    bilirubin = serializers.FloatField(required=False)
    clarity = serializers.CharField(required=False)
    color = serializers.CharField(required=False)
    glucose = serializers.FloatField(required=False)   
    glucose1 = serializers.FloatField(required=False)  
    hemoglobin = serializers.FloatField(required=False)
    ketones = serializers.FloatField(required=False)
    leukocytes = serializers.FloatField(required=False)   
    nitrite = serializers.FloatField(required=False)
    ph = serializers.FloatField(required=False)
    protein = serializers.FloatField(required=False)   
    specific_gravity = serializers.FloatField(required=False)
    urobilinogen = serializers.FloatField(required=False)









from rest_framework import serializers
from .models import Patient, Document, Vital,Medication,LabResult

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ["id", "first_name", "last_name", "email", "phone"]

class DocumentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    patient_id = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all(), source="patient", write_only=True
    )

    class Meta:
        model = Document
        fields = [
            "id",
            "name",
            "description",
            "category",
            "file",
            "created_at",
            "updated_at",
            "patient",
            "patient_id",
        ]


class VitalSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    patient_id = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all(), source="patient", write_only=True
    )

    class Meta:
        model = Vital
        fields = [
            "id",
            "vital_type",
            "value",
            "value1",
            "unit",
            "recorded_at",
            "metadata",
            "created_at",
            "updated_at",
            "patient",
            "patient_id",
        ]


class MedicationSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    patient_id = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all(), source="patient", write_only=True
    )

    class Meta:
        model = Medication
        fields = [
            "id",
            "medicine",
            "type",
            "sig",
            "qty",
            "unit",
            "refills",
            "days",
            "created_at",
            "updated_at",
            "patient",
            "patient_id",
        ]



class LabResultSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    patient_id = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all(), source="patient", write_only=True
    )

    class Meta:
        model = LabResult
        fields = [
            "id",
            "lab_result_for",
            "abnormal_flag",
            "value",
            "note",
            "recorded_at",
            "file",
            "file_type",
            "created_at",
            "updated_at",
            "patient",
            "patient_id",
        ]
