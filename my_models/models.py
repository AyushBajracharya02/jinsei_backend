from django.db import models
from django.core.validators import RegexValidator
from datetime import date
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.postgres.fields import ArrayField

nameRegex = r"^[a-zA-Z]{2,32}$"
phoneRegex = r"^\d{10}$"
passwordRegex = r"^.{8,32}$"

name_validator = RegexValidator(
    regex=nameRegex,
    message="Name should only contain letters and be between 2 and 32 characters.",
    code="invalid_name",
)

phone_validator = RegexValidator(
    regex=phoneRegex,
    message="Phone should only contain numbers and should be 10 characters",
    code="invalid_phone_number",
)

password_validator = RegexValidator(
    regex=passwordRegex,
    message="Password should be between 8 and 32 characters",
    code="invalid_password",
)

BLOOD_GROUPS = (
    ("A+", "A+"),
    ("B+", "B+"),
    ("AB+", "AB+"),
    ("O+", "O+"),
    ("A-", "A-"),
    ("B-", "B-"),
    ("AB-", "AB-"),
    ("O-", "O-"),
)


SEX_CHOICES = (
    ("M", "Male"),
    ("F", "Female"),
    ("O", "Other"),
)


class AppUser(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(
        max_length=32, null=True, blank=True, validators=[name_validator]
    )
    lastname = models.CharField(
        max_length=32, null=True, blank=True, validators=[name_validator]
    )
    phonenumber = models.CharField(max_length=10, validators=[phone_validator])
    password = models.CharField(max_length=32, validators=[password_validator])
    address = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    bloodgroup = models.CharField(
        max_length=4,
        choices=BLOOD_GROUPS,
        null=True,
        blank=True,
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    age = models.IntegerField(
        null=True,
        blank=True,
    )
    sex = models.CharField(null=True, max_length=1, choices=SEX_CHOICES)
    mealschedule = models.JSONField(default=dict)

    def save(self, *args, **kwargs):
        if self.date_of_birth:
            today = date.today()
            self.age = (
                today.year
                - self.date_of_birth.year
                - (
                    (today.month, today.day)
                    < (self.date_of_birth.month, self.date_of_birth.day)
                )
            )
        super(AppUser, self).save(*args, **kwargs)

    class Meta:
        db_table = "jinsei_user"


class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(
        max_length=32, null=True, blank=True, validators=[name_validator]
    )
    lastname = models.CharField(
        max_length=32, null=True, blank=True, validators=[name_validator]
    )
    phonenumber = models.CharField(
        max_length=10, null=True, blank=True, validators=[phone_validator]
    )
    password = models.CharField(
        max_length=32, null=True, blank=True, validators=[password_validator]
    )
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    schedule = models.JSONField(null=True, blank=True)
    mealschedule = models.JSONField(null=True, blank=True)
    address = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )
    bloodgroup = models.CharField(
        max_length=3,
        choices=BLOOD_GROUPS,
        null=True,
        blank=True,
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    age = models.IntegerField(
        null=True,
        blank=True,
    )
    sex = models.CharField(null=True, max_length=1, choices=SEX_CHOICES)

    def save(self, *args, **kwargs):
        if self.date_of_birth:
            today = date.today()
            self.age = (
                today.year
                - self.date_of_birth.year
                - (
                    (today.month, today.day)
                    < (self.date_of_birth.month, self.date_of_birth.day)
                )
            )
        super(Doctor, self).save(*args, **kwargs)

    class Meta:
        db_table = "doctor"


class Appointment(models.Model):
    content_type = models.ForeignKey(ContentType, null=True, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(null=True)
    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE)
    patient = GenericForeignKey("content_type", "object_id")
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True)

    class Meta:
        db_table = "appointment"

class Prescription(models.Model):
    id = models.AutoField(primary_key=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    pulse_rate = models.IntegerField()
    blood_pressure = ArrayField(models.DecimalField(max_digits=3, decimal_places=0),null=True)
    oxygen_level = models.DecimalField(max_digits=5, decimal_places=2)
    medication = ArrayField(models.JSONField())
    createddate = models.DateField(null=True,blank=True)

    class Meta:
        db_table = "prescription"

class Medicine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        db_table = "medicine"
