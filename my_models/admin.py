from django.contrib import admin
from my_models.models import AppUser, Doctor, Appointment, Medicine, Prescription

class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'appointment', 'weight', 'temperature', 'pulse_rate', 'blood_pressure', 'oxygen_level', 'medication', 'createddate')

admin.site.register(Prescription, PrescriptionAdmin)


admin.site.register(AppUser)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Medicine)