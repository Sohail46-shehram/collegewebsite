from django.db import models
from django.contrib.auth.models import User


class AdmissionApplication(models.Model):

    PROGRAM_TYPE = [
        ("ADP", "ADP"),
        ("BS", "BS"),
    ]

    PROGRAM_CHOICES = [
        ("ADP Information Technology", "ADP Information Technology"),
        ("ADP Commerce", "ADP Commerce"),
        ("ADP Arts", "ADP Arts"),
        ("ADP English", "ADP English"),
        ("ADP Education", "ADP Education"),
        ("ADP Social Work", "ADP Social Work"),

        ("BS Urdu", "BS Urdu"),
        ("BS English", "BS English"),
        ("BS Political Science", "BS Political Science"),
        ("BS Economics", "BS Economics"),
        ("BS Zoology", "BS Zoology"),
        ("BS Botany", "BS Botany"),
        ("BS Islamic Studies", "BS Islamic Studies"),
        ("BS Physics", "BS Physics"),
        ("BS Chemistry", "BS Chemistry"),
    ]

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=150)
    father_name = models.CharField(max_length=150)
    cnic = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()

    program_type = models.CharField(max_length=20, choices=PROGRAM_TYPE)
    program = models.CharField(max_length=100, choices=PROGRAM_CHOICES)

    matric_board = models.CharField(max_length=100)
    matric_total_marks = models.IntegerField()
    matric_obtained_marks = models.IntegerField()

    inter_board = models.CharField(max_length=100)
    inter_total_marks = models.IntegerField()
    inter_obtained_marks = models.IntegerField()

    photo = models.ImageField(upload_to="student_photos/")
    matric_result_card = models.FileField(upload_to="documents/matric/")
    inter_result_card = models.FileField(upload_to="documents/inter/")
    cnic_file = models.FileField(upload_to="documents/cnic/")
    matric_percentage = models.FloatField(default=0)
    inter_percentage = models.FloatField(default=0)
    merit_percentage = models.FloatField(default=0)
    merit_position = models.IntegerField(null=True, blank=True)
    is_merit_published = models.BooleanField(default=False)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    applied_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.matric_total_marks > 0:
            self.matric_percentage = (
                self.matric_obtained_marks / self.matric_total_marks
            ) * 100

        if self.inter_total_marks > 0:
            self.inter_percentage = (
                self.inter_obtained_marks / self.inter_total_marks
            ) * 100

        self.merit_percentage = (
            self.matric_percentage * 0.30
            + self.inter_percentage * 0.70
        )

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name} - {self.program}"
    MERIT_STATUS = [
    ("Not Published", "Not Published"),
    ("Published", "Published"),
]

