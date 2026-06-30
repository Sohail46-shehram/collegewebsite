from django import forms
from .models import AdmissionApplication


class AdmissionApplicationForm(forms.ModelForm):
    class Meta:
        model = AdmissionApplication

        fields = [
            "full_name",
            "father_name",
            "cnic",
            "phone",
            "email",
            "address",
            "program_type",
            "program",
            "matric_board",
            "matric_total_marks",
            "matric_obtained_marks",
            "inter_board",
            "inter_total_marks",
            "inter_obtained_marks",
            "photo",
            "matric_result_card",
            "inter_result_card",
            "cnic_file",
        ]